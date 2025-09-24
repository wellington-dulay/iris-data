import pandas as pd

def import_data():
    # Load the dataset
    data = pd.read_csv("iris-data/iris/iris.data", header=None)
    # Convert 'Category' column to categorical type
    data[4] = data[4].astype('category')
    return data

def main():
    data = import_data()
    print(data.head())

if __name__ == "__main__":
    main()