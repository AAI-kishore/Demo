from sklearn import svm
from sklearn import datasets

iris = datasets.load_iris()

X,y = iris.data, iris.target

clf = svm.SVC()
clf.fit(X,y)

import pickle

# with open('model.pkl','wb') as f:
#     pickle.dump(clf,f)

pickle.dump(clf, open('knn_model.pkl','wb'))

# with open('model.pkl','rb') as f:
#     clf2 = pickle.load(f)

# print(clf2.predict(X[20:23]))