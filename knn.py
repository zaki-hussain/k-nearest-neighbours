import numpy as np
import pandas as pd


class KNN:
    def __init__(self, k):
        self.k = k
    
    def fit(self, x_train, y_train):
        self.x_train = x_train
        self.y_train = y_train

    def predict(self, new_data_point):
        self.new_data_point = new_data_point
        self.distances = np.sqrt(np.sum((self.x_train-self.new_data_point)**2, axis=1))
        self.ordered_indices = np.argsort(self.distances)
        print(self.y_train[self.ordered_indices][:self.k])


df = pd.read_csv("iris.csv")
df = df.drop("Id", axis=1)
y_train = np.array([])

for i in df.index:
    match df.loc[i, "Species"]:
        case "Iris-setosa":
            y_train = np.append(y_train,[0])
        case "Iris-versicolor":
            y_train = np.append(y_train,[1])
        case "Iris-virginica":
            y_train = np.append(y_train,[2])

df = df.drop("Species", axis=1)
x_train = df.to_numpy()

iris_classifier = KNN(int(input("What value should k be?\n")))
iris_classifier.fit(x_train,y_train)

new_data_point = np.array([float(input("What is the sepal length (cm)?\n")),float(input("What is the sepal width (cm)\n")),float(input("What is the petal length (cm)?\n")),float(input("What is the petal width (cm)?\n"))])

iris_classifier.predict(new_data_point)