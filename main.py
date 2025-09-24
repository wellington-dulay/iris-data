import pandas as pd

data = pd.read_csv("iris-data\iris\iris.data", header=None)

print(data.head())
print(data.describe())