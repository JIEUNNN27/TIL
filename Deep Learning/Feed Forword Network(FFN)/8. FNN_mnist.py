# -*- coding: utf-8 -*-
"""1. 코드만.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sSA28FGOfFCFetqXX4FTRT4RKfaEveZh
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle

DATA_PATH = '/content/drive/MyDrive/Colab Notebooks/data/mnist/'

with open(DATA_PATH + 'mnist.pkl', 'rb') as f:
        mnist = pickle.load(f)

print(mnist.keys())

#0~255 -> 0~1.0 숫자의 범위를 변환한다
x_feat = np.array(mnist['data'])/255
#2차원(2d) 구조로 다시 만들어주는 reshape
y_target = np.array(mnist['target']).astype('int8').reshape(-1, 1)
#str으로 되어 있난 target int로 바꿔주기
#y_target = mnist.target.to_numpy().astype('int8').reshape(-1, 1)

#데이터 나누기
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x_feat, y_target, test_size = 0.2)

#클래스 갯수
n_class = len(set(mnist['target']))
n_class

from tensorflow.keras.layers import Input, Dense
from tensorflow.keras import Model

"""# 첫번째

- 은닉층 1개
- batch 20, epoch 30
"""

#softmax 이용하기

#입력층
xInput = Input(batch_shape = (None, x_train.shape[1]))

#은닉층
hLayer = Dense(10)(xInput)

#출력층
yOutput = Dense(n_class, activation = "softmax")(hLayer)
#yOutput = Dense(len(mnist.target.unique()), ...)

#yOutput = Dense(y_train.shape[1], activation = "softmax")(hLayer)

model = Model(xInput, yOutput)
model.compile(loss = 'sparse_categorical_crossentropy', optimizer = 'adam')

hist = model.fit(x_train, y_train, batch_size = 20, epochs = 30,
                 validation_data = (x_test, y_test))

#error 관찰
plt.plot(hist.history['loss'], label = 'Train loss')
plt.plot(hist.history['val_loss'], label = 'Test loss')
plt.legend()
plt.title("Loss function")
plt.xlabel("epoch")
plt.ylabel("loss")
plt.show

#평가
y_prob = model.predict(x_test)

y_pred = np.argmax(y_prob,axis=1).reshape(-1, 1)

acc = (y_test == y_pred).mean()
print(acc)

"""# tuning 1

- 은닉층 1개 
- batch 100개, epoch 100
"""

#softmax 이용하기

#입력층
xInput = Input(batch_shape = (None, x_train.shape[1]))

#은닉층
hLayer = Dense(10)(xInput)

#출력층
yOutput = Dense(n_class, activation = "softmax")(hLayer)
#yOutput = Dense(len(mnist.target.unique()), ...)

#yOutput = Dense(y_train.shape[1], activation = "softmax")(hLayer)

model2 = Model(xInput, yOutput)
model2.compile(loss = 'sparse_categorical_crossentropy', optimizer = 'adam')

hist = model2.fit(x_train, y_train, batch_size = 100, epochs = 100,
                 validation_data = (x_test, y_test))

#error 관찰
plt.plot(hist.history['loss'], label = 'Train loss')
plt.plot(hist.history['val_loss'], label = 'Test loss')
plt.legend()
plt.title("Loss function")
plt.xlabel("epoch")
plt.ylabel("loss")
plt.show

#평가
y_prob = model2.predict(x_test)

y_pred = np.argmax(y_prob,axis=1).reshape(-1, 1)

acc = (y_test == y_pred).mean()
print(acc)

"""# tuning2

- 은닉층 1개
- batch 100, epoch 50
"""

#softmax 이용하기

#입력층
xInput = Input(batch_shape = (None, x_train.shape[1]))

#은닉층
hLayer = Dense(10)(xInput)

#출력층
yOutput = Dense(n_class, activation = "softmax")(hLayer)
#yOutput = Dense(len(mnist.target.unique()), ...)

#yOutput = Dense(y_train.shape[1], activation = "softmax")(hLayer)

model3 = Model(xInput, yOutput)
model3.compile(loss = 'sparse_categorical_crossentropy', optimizer = 'adam')

hist = model3.fit(x_train, y_train, batch_size = 100, epochs = 50,
                 validation_data = (x_test, y_test))

#error 관찰
plt.plot(hist.history['loss'], label = 'Train loss')
plt.plot(hist.history['val_loss'], label = 'Test loss')
plt.legend()
plt.title("Loss function")
plt.xlabel("epoch")
plt.ylabel("loss")
plt.show

#평가
y_prob = model3.predict(x_test)

y_pred = np.argmax(y_prob,axis=1).reshape(-1, 1)

acc = (y_test == y_pred).mean()
print(acc)

"""# Tuning3

- 은닉층 1개
- batch 50, epoch 50
"""

#softmax 이용하기

#입력층
xInput = Input(batch_shape = (None, x_train.shape[1]))

#은닉층
hLayer = Dense(10)(xInput)

#출력층
yOutput = Dense(n_class, activation = "softmax")(hLayer)
#yOutput = Dense(len(mnist.target.unique()), ...)

#yOutput = Dense(y_train.shape[1], activation = "softmax")(hLayer)

model4 = Model(xInput, yOutput)
model4.compile(loss = 'sparse_categorical_crossentropy', optimizer = 'adam')

hist = model4.fit(x_train, y_train, batch_size = 50, epochs = 50,
                 validation_data = (x_test, y_test))

#error 관찰
plt.plot(hist.history['loss'], label = 'Train loss')
plt.plot(hist.history['val_loss'], label = 'Test loss')
plt.legend()
plt.title("Loss function")
plt.xlabel("epoch")
plt.ylabel("loss")
plt.show

#평가
y_prob = model4.predict(x_test)

y_pred = np.argmax(y_prob,axis=1).reshape(-1, 1)

acc = (y_test == y_pred).mean()
print(acc)

"""#tuning4

- 은닉층 1개
- batch 50, epoch 30
"""

#softmax 이용하기

#입력층
xInput = Input(batch_shape = (None, x_train.shape[1]))

#은닉층
hLayer = Dense(10)(xInput)

#출력층
yOutput = Dense(n_class, activation = "softmax")(hLayer)
#yOutput = Dense(len(mnist.target.unique()), ...)

#yOutput = Dense(y_train.shape[1], activation = "softmax")(hLayer)

model5 = Model(xInput, yOutput)
model5.compile(loss = 'sparse_categorical_crossentropy', optimizer = 'adam')

hist = model5.fit(x_train, y_train, batch_size = 50, epochs = 30,
                 validation_data = (x_test, y_test))

#error 관찰
plt.plot(hist.history['loss'], label = 'Train loss')
plt.plot(hist.history['val_loss'], label = 'Test loss')
plt.legend()
plt.title("Loss function")
plt.xlabel("epoch")
plt.ylabel("loss")
plt.show

#평가
y_prob = model5.predict(x_test)

y_pred = np.argmax(y_prob,axis=1).reshape(-1, 1)

acc = (y_test == y_pred).mean()
print(acc)

"""# Tuning5
- 은닉층3개
- batch 50 epoch 30
"""

#softmax 이용하기

#입력층
xInput = Input(batch_shape = (None, x_train.shape[1]))

#은닉층
hLayer1 = Dense(10)(xInput)
hLayer2 = Dense(10)(hLayer1)
hLayer3 = Dense(10)(hLayer2)

#출력층
yOutput = Dense(n_class, activation = "softmax")(hLayer3)
#yOutput = Dense(len(mnist.target.unique()), ...)

#yOutput = Dense(y_train.shape[1], activation = "softmax")(hLayer)

model6 = Model(xInput, yOutput)
model6.compile(loss = 'sparse_categorical_crossentropy', optimizer = 'adam')

hist = model6.fit(x_train, y_train, batch_size = 50, epochs = 30,
                 validation_data = (x_test, y_test))

#error 관찰
plt.plot(hist.history['loss'], label = 'Train loss')
plt.plot(hist.history['val_loss'], label = 'Test loss')
plt.legend()
plt.title("Loss function")
plt.xlabel("epoch")
plt.ylabel("loss")
plt.show

#평가
y_prob = model6.predict(x_test)

y_pred = np.argmax(y_prob,axis=1).reshape(-1, 1)

acc = (y_test == y_pred).mean()
print(acc)