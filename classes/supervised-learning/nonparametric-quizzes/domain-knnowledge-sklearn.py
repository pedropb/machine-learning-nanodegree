from sklearn.neighbors import KNeighborsClassifier as KNN
import numpy as np


X_train = [[1,6], [2,4], [3,7], [6,8], [7,1], [8,4]]
y_train = [7,8,16,44,50,68]

euc1 = KNN(n_neighbors=1, p=2, algorithm='brute', weights='uniform')
euc1.fit(X_train, y_train)
print "euc1: ", euc1.predict([[4,2]])
print "euc1_neighbors: ", euc1.kneighbors([[4,2]], return_distance=False)

euc3 = KNN(n_neighbors=3, p=2, algorithm='brute', weights='uniform')
euc3.fit(X_train, y_train)
print "euc3: ", euc3.predict([[4,2]])
print "euc3_neighbors: ", euc3.kneighbors([[4,2]], return_distance=False)

man1 = KNN(n_neighbors=2, p=1, algorithm='brute', weights='uniform')
man1.fit(X_train, y_train)
print "man1: ", man1.predict([[4,2]])
print "man1_neighbors: ", man1.kneighbors([[4,2]], return_distance=False)

man3 = KNN(n_neighbors=4, p=1, algorithm='brute', weights='uniform')
man3.fit(X_train, y_train)
print "man3: ", man3.predict([[4,2]])
print "man3_neighbors: ", man3.kneighbors([[4,2]], return_distance=False)

# These outputs are not the expected answer to the quiz.