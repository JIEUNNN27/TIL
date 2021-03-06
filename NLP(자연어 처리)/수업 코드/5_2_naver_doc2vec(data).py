# -*- coding: utf-8 -*-
"""5-2.naver_doc2vec(data).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/175V0gjlvVslSYMWN6iZPj13oxgZW-TTM
"""

!pip install sentencepiece

import pandas as pd
import numpy as np
import sentencepiece as spm
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from tensorflow.keras.preprocessing.sequence import pad_sequences
import re
import pickle

# Commented out IPython magic to ensure Python compatibility.
# %cd '/content/drive/My Drive/Colab Notebooks'

train_data = pd.read_csv('data/naver_movie/ratings_train.txt', sep='\t')
test_data = pd.read_csv('data/naver_movie/ratings_test.txt', sep='\t')
train_data = train_data.dropna()
test_data = test_data.dropna()

train_data.head()

# 기호, 숫자, 영어 등은 제외하고 한글만 사용한다.
train_list = [re.sub("[^가-힣ㄱ-ㅎㅏ-ㅣ\s]", "", x) for x in train_data['document']]
test_list = [re.sub("[^가-힣ㄱ-ㅎㅏ-ㅣ\s]", "", x) for x in test_data['document']]

n_train = len(train_list)
n_test = len(test_list)

# Sentencepice용 사전을 만들기 위해 train_list, test_list를 저장해 둔다.
data_file = "data/naver_data.txt"
with open(data_file, 'w', encoding='utf-8') as f:
    for sent in train_list + test_list:
        f.write(sent + '\n')
        
# Google의 Sentencepiece를 이용해서 vocabulary를 생성한다.
templates= "--input={} \
            --pad_id=0 --pad_piece=<PAD>\
            --unk_id=1 --unk_piece=<UNK>\
            --bos_id=2 --bos_piece=<BOS>\
            --eos_id=3 --eos_piece=<EOS>\
            --model_prefix={} \
            --vocab_size={}"

VOCAB_SIZE = 10000
model_prefix = "data/naver_model"
params = templates.format(data_file, model_prefix, VOCAB_SIZE)

spm.SentencePieceTrainer.Train(params)
sp = spm.SentencePieceProcessor()
sp.Load(model_prefix + '.model')

with open(model_prefix + '.vocab', encoding='utf-8') as f:
    vocab = [doc.strip().split('\t') for doc in f]

word2idx = {k:v for v, [k, _] in enumerate(vocab)}
idx2word = {v:k for v, [k, _] in enumerate(vocab)}

# 문서를 서브 워드로 분해한다.
train_subword = [sp.encode_as_pieces(x) for x in train_list]
test_subword = [sp.encode_as_pieces(x) for x in test_list]

train_subword[0]

# test data까지 학습에 이용하는 것은 데이터 분석의 정석은 아니다.
# 정석대로 하려면 train data로만 doc2vec을 학습하고, test data는 inference stage로
# 추정해야 한다. 그러나 kaggle 형태의 공모전에서는 test data의 feature 부분을 이용하는 
# 것은 허용된다. 데이터를 표준화할 때 test data의 feature 부분을 이용하는 것과 동일하다.
# 이 코드는 doc2vec의 기능 시험을 위한 것으로 test data까지 포함해서 doc2vec을 학습시켜 본다.
tag_sent = [TaggedDocument(x, [i]) for i, x in enumerate(train_subword + test_subword)]
tag_sent[0]

model = Doc2Vec(tag_sent, vector_size=32, window=5, min_count=1)

d_vector = [model.docvecs[tags[0]] for _, tags in tag_sent]

x_train = np.array(d_vector[:n_train])
x_test = np.array(d_vector[n_train:])
x_train.shape, x_test.shape

y_train = np.array(train_data['label'])
y_test = np.array(test_data['label'])

y_train.shape, y_test.shape

# 학습 데이터를 저장해 둔다.
with open('data/naver_doc2vec.pkl', 'wb') as f:
    pickle.dump([x_train, x_test, y_train, y_test], f, pickle.DEFAULT_PROTOCOL)

