# -*- coding: utf-8 -*-
"""movieLens(matrix).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MzX3PE1TAMTScX_8qQMyQX17pUL8MRdp
"""

# 행렬 분해를 이용한 잠재 요인 협업 필터링
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import numba as nb

# 학습 데이터를 읽어온다.
DATA_PATH = '/content/drive/My Drive/Colab Notebooks/data/'
movies = pd.read_csv(DATA_PATH + 'MovieLens/movies.csv')
ratings = pd.read_csv(DATA_PATH + 'MovieLens/ratings.csv')
movies.head()

ratings.head()

print('user 수 =', len(set(ratings['userId'])))
print('movie 개수 =', len(set(ratings['movieId'])))
print('user number = {} ~ {}'.format(ratings['userId'].min(), ratings['userId'].max()))
print('movie number = {} ~ {}'.format(ratings['movieId'].min(), ratings['movieId'].max()))

df = pd.merge(ratings, movies, on='movieId')[['userId', 'movieId', 'rating', 'title']]

# movieId가 중간에 빈 값이 많으므로 순차적인 id를 다시 부여한다.
item_enc = LabelEncoder()

df['userId'] -= 1
df['movieId'] = item_enc.fit_transform(df['movieId'])
df['rating'] /= 5.0   # 0.5 ~ 5.0 --> 0.1 ~ 1.0으로 표준화.

# movieId = 163937은 movieId = 9371로 변환되었다.
# item_enc.transform([163937])[0] = 9371
# item_enc.inverse_transform([9371])[0] = 163937
df.head()

print('user 수 =', len(set(df['userId'])))
print('movie 개수 =', len(set(df['movieId'])))
print('user number = {} ~ {}'.format(df['userId'].min(), df['userId'].max()))
print('movie number = {} ~ {}'.format(df['movieId'].min(), df['movieId'].max()))

# pivoting
UR = np.array(df.pivot_table('rating', index='userId', columns='movieId'))

# number of users and items
N_ROW = UR.shape[0]
N_COL = UR.shape[1]
N_ROW, N_COL

UR[0, 0], UR[4,0], UR[14,0], UR[16,0]

@nb.jit
# SGD로 행렬 F, B를 업데이트한다.
def update_matrix(R, F, B, a, r):
    for i in range(N_ROW):
        for j in range(N_COL):
            if np.isnan(R[i, j]) != True:  # nan이 아니면
                # error 항을 계산한다.
                eij = R[i, j] - np.dot(F[i, :], B[j, :])
    
                # update F, B
                F[i, :] += a * (eij * B[j, :] - r * F[i, :])
                B[j, :] += a * (eij * F[i, :] - r * B[j, :])

@nb.jit
# NaN이 포함된 행렬의 mean_squared_error를 계산한다.
# 행렬 x에는 NaN이 포함돼 있다. y에는 없다.
def mse_skip_nan(x, y):
    mse = 0.0
    cnt = 0
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            if np.isnan(x[i, j]) != True:  # nan이 아니면
                mse += (x[i, j] - y[i, j]) ** 2
                cnt += 1
    return mse / cnt

# SGD로 행렬을 F, B로 분해한다.
def factorize_matrix(matR, k, max_iter=1000, alpha=0.01, beta=0.01, err_limit=1e-4):
    # F, B를 random 초기화한다.
    F = np.random.rand(N_ROW, k)  # factor matrix
    B = np.random.rand(N_COL, k)  # beta matrix.
 
    old_err = 9999   # error 초깃값
    err_hist = []    # error history
    for step in range(max_iter):
        # F, B를 업데이트한다.
        update_matrix(matR, F, B, alpha, beta)
        
        # error를 계산하고 저장해 둔다.
        err = mse_skip_nan(matR, np.dot(F, B.T))
        err_hist.append(err)

        # early stopping
        if np.abs(old_err - err) < err_limit:
            break
        
        old_err = err
        
        if step % 10 == 0:
            print('{} : error={:.4f}'.format(step, err))

    if step >= max_iter - 1:
        print('max_iter={}번 동안 stop하지 못했습니다.'.format(max_iter))
        print('max_iter를 늘리거나 err_limit을 늘려야 합니다.')
        
    return F, B.T, err_hist

K = 10  # number of factors
F, B, err = factorize_matrix(UR, k=K, max_iter=100)

# 타겟 유저가 보지 않은 영화들에 대해 해당 유저가 부여할 rating을 추정한다.
target_user = 9
user_id = target_user - 1     # 위에서 userId가 0부터 시작하기 위해 1을 뺐었음.
top_n = 10                    # 추정 평정이 높은 상위 top_n개

# target user가 안 본 영화의 인덱스와 추정 rating
ER = np.dot(F, B)   # estimated R
unseen_idx = np.where(np.isnan(UR[0, :]))[0]
pred_R = ER[user_id, unseen_idx]

# target user에게 추천할 영화 리스트
recom_idx = np.array(pred_R).argsort()[::-1][:top_n]

print('\n영화 추천 목록 : User = {}'.format(target_user))
print("--- {:s} {:s}".format('-' * 35, '-' * 15))
print("No  {:35s} {:s}".format('Title', 'Expected rating'))
print("--- {:s} {:s}".format('-' * 35, '-' * 15))
for i, p in enumerate(recom_idx):
    title = df[df['movieId'] == unseen_idx[p]]['title'].values[0]

    # rating: 0.1 ~ 1.0 --> 0.5 ~ 5.0으로 복원한다.
    print("{:2d} : {:40s}{:.4f}".format(i+1, title[:39], pred_R[p] * 5.0))
print("{:s}".format('-' * 55))

