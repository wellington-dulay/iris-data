import pandas as pd

def import_data(path):
    # Load the dataset
    data = pd.read_csv(path, header=None)
    return data

def main():
    data = import_data("iris-data/iris/iris.data")
    print(data.head())