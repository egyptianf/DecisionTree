from fileIO import FileIO
from preprocess import Preprocessing


if __name__ == '__main__':
    filename = 'house-votes-84.data.txt'
    fileio = FileIO()
    data = fileio.read_csv(filename)

    preprocessing = Preprocessing()
    preprocessing.assume_missing_values(data)

    training_data, testing_data = preprocessing.split_into_training_and_testing(data, 0.3)
    print("Training: ", training_data)
    print("Testing", testing_data)