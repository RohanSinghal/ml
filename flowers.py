#!/usr/bin/python3

import time
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

#loading iris

iris = load_iris()

#print flower naqmes

fl_name = iris.target_names

#print features of iris

fl_features = iris.feature_names

# loading flower features data

fl_features_data = iris.data

#print(fl_features_data)
fl_real_data = iris.target

plt.xlabel("setosa")
plt.ylabel("versicolor")
plt.title("IRIS")
x1=fl_features_data[0:50]
y1=fl_features_data[0:50]
plt.legend()
plt.show()
