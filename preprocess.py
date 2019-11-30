import math


class Preprocessing:

    def split_into_training_and_testing(self, data, training_ratio):
        """

        :rtype: list, list
        """
        training_index = math.floor(training_ratio * len(data))
        training = data[0:training_index]
        testing = data[training_index:]
        return training, testing


    def assume_missing_values(self, data):

        counters = []
        # First is for YES and second is for NO
        for i in range(len(data[0])):
            counters.append([0, 0])



        for row in data:
            for i in range(len(row)):
                if i == 0:
                    continue
                else:
                    if row[i] == 'y':
                        counters[i][0] += 1
                    elif row[i] == 'n':
                        counters[i][1] += 1

        for row in data:
            for i in range(len(row)):
                if i == 0:
                    continue
                else:
                    if row[i] == '?':
                        row[i] = 'y' if counters[i][0] > counters[i][1] else 'n'

        return data
