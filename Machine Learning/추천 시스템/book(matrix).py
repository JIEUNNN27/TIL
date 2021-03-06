# -*- coding: utf-8 -*-
"""book(matrix).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bMp_-dqVH9RFI9ERic5w-3dvhuueI8kq
"""

# 행렬 분해를 이용한 잠재 요인 협업 필터링
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import numba as nb

# Book 데이터를 읽어온다. 데이터 url : https://www.kaggle.com/arashnic/book-recommendation-dataset
DATA_PATH = '/content/drive/My Drive/Colab Notebooks/data/'
books = pd.read_csv(DATA_PATH + 'book/Books.csv')[['ISBN', 'Book-Title', 'Image-URL-M']]
ratings = pd.read_csv(DATA_PATH + 'book/Ratings.csv')

books.shape, ratings.shape

books.head()

ratings.head()

# 추천 책들의 이미지를 표시한다.

