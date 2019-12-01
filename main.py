from fileIO import FileIO
from preprocess import Preprocessing
from decisionTree import DecisionTree


if __name__ == '__main__':
    filename = 'house-votes-84.data.txt'
    fileio = FileIO()
    data = fileio.read_csv(filename)

    preprocessing = Preprocessing()
    preprocessing.assume_missing_values(data)
    for percent in range(3, 8):
        training_data, testing_data = preprocessing.split_into_training_and_testing(data, percent/float(10))
        attributes_number = len(training_data[0]) - 1
        decision_tree = DecisionTree()
        root_node = decision_tree.build(training_data)
        # decision_tree.print()
        # print("Classification: ")
        accuracy = 0
        for row in testing_data:
            classified = decision_tree.classify(row, decision_tree.root)
            classified.calc_percentages(len(testing_data))
            if classified.republicans_percent > 50.0 and row[0] == 'republican' or (
                    classified.democrats_percent > 50.0 and row[0] == 'democrat'):
                accuracy += 1

        accuracy = accuracy / float(len(testing_data))
        print("Accuracy using training data", percent/float(10)*100, "% is: ", accuracy)
