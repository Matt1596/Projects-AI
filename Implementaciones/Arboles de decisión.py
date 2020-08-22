from sklearn import tree
from sklearn.datasets import load_boston
import numpy as np

import graphviz

Boston = load_boston()


classifier = tree.DecisionTreeClassifier()

X = Boston["data"]
Y = Boston["target"]
np.set_printoptions(threshold=np.nan)
#X = np.round(X)

##COMO EL DATASET DE BOSTON TIENE UN TARGET DE TIPO CONTINUO, DISCRETIZAMOS CON 3 CLASES, MEDIA BAJA, NORMAL Y ALTA (0,1,2) PARA (0-15, 15-30 , 30-9999)

bins = [0, 15, 30, 99999]
labels = [0, 1, 2]
#print (Y)

import pandas as pd
Y = pd.cut(Y, bins=bins, labels=labels)
Y = Y.astype('int64')

classifier_trained = classifier.fit(X, Y)

test1 = [10, 15, 20, 35, 5, 1, 7, 100, 5.09, 3.52, 1., 0.201, 1.5]

pred = classifier_trained.predict_proba([test1])
print(pred)

X_true = X[:65]
Y_true = Y[:65]

X_learn = X[65:]
Y_learn = Y[65:]

Y_predict = classifier.predict(X_true)

print("Y True vs Y Predict:")
print(Y_true)
print(Y_predict)

print("CM Y SSE:")

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(Y_true, Y_predict)
print(cm)
from sklearn.metrics import mean_squared_error
print("SSE:", mean_squared_error(Y_true, Y_predict))




dot_data = tree.export_graphviz(classifier_trained, out_file=None,
                                filled=True, rounded=True)

graph = graphviz.Source(dot_data)
graph.render('Boston', view=True)