from fileIO import FileIO
from preprocess import Preprocessing
from decisionTree import DecisionTree

if __name__ == '__main__':
    filename = 'house-votes-84.data.txt'
    fileio = FileIO()
    data = fileio.read_csv(filename)

    preprocessing = Preprocessing()
    preprocessing.assume_missing_values(data)

    training_data, testing_data = preprocessing.split_into_training_and_testing(data, 0.3)
    attributes_number = len(training_data[0]) - 1
    print("training data length: ", len(training_data))
    tree = DecisionTree()

    # Suppose we want to see the information gain for all attributes
    print("best attribute to split on is: ", tree.get_best_attr_to_split_on(training_data, attributes_number))
