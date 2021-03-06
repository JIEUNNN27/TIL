# -*- coding: utf-8 -*-
"""4.Bagging.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1w46xFKQOAZKeTIrvr2UPhHZsqdLKw_i8
"""

# Bagging에 의한 앙상블 방법을 연습한다.
# ------------------------------------
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import BaggingClassifier
import numpy as np
from sklearn.metrics import classification_report

# iris 데이터를 읽어온다.
iris = load_iris()

# Train 데이터 세트와 Test 데이터 세트를 구성한다
x_train, x_test, y_train, y_test = train_test_split(iris['data'], iris['target'], test_size = 0.2)

# 4가지 모델을 생성한다 (KNN, Decision tree, SVM, Logistic Regression).
knn = KNeighborsClassifier(n_neighbors=5, p=2, metric='minkowski')
dtree = DecisionTreeClassifier(criterion='gini', max_depth=8)
svm = SVC(kernel='rbf', gamma=0.1, C=1.0, probability=True)
lreg = LogisticRegression(max_iter=500)

# 4가지 모델로 Bagging을 구성하고, 각 모델의 추정 확률을 누적한다.
prob = np.zeros((y_test.shape[0], iris.target_names.shape[0]))
base_model = [knn, dtree, svm, lreg]
for m in base_model:
    bag = BaggingClassifier(base_estimator=m, n_estimators=100)
    bag.fit(x_train, y_train)
    
    prob += bag.predict_proba(x_test)

# 확률의 누적합이 가장 큰 class를 찾고, 정확도를 측정한다.
y_pred = np.argmax(prob, axis=1)

# 시험데이터의 confusion matrix를 작성한다 (row : actual, col : predict)
print('\nConfusion matrix :')
print(confusion_matrix(y_test, y_pred))
print()
print(classification_report(y_test, y_pred, target_names=iris.target_names))

