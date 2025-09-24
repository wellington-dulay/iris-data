import pandas as pd
import matplotlib.pyplot as plt

def import_data():
    # Load the dataset
    data = pd.read_csv("iris-data/iris/iris.data", header=None)
    # Convert 'Category' column to categorical type
    data[4] = data[4].astype('category')
    return data

def calculate_summary_statistics(data):
    # Calculate summary statistics
    summary = data.describe()
    return summary

def class_distribution(data):
    # Calculate class distribution
    distribution = data[4].value_counts()
    return distribution

def class_histogram(data):
    # Plot histogram of class distribution
    for iris_class in data[4].unique():
        subset = data[data[4] == iris_class]
        plt.hist(subset[0], alpha=0.5, label=iris_class)
        plt.legend(title="Class")
        plt.xlabel("Sepal Length")
        plt.ylabel("Frequency")
        plt.title("Class Histogram")
        plt.savefig("class_histogram_" + iris_class + ".png")
        plt.clf()

def main():
    data = import_data()
    print(calculate_summary_statistics(data))
    print(class_distribution(data))
    class_histogram(data)   

if __name__ == "__main__":
    main()