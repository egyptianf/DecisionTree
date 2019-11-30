import math


class Preprocessing:
    counters = []


    def split_into_training_and_testing(self, data, training_ratio):
        """

        :rtype: list, list
        """
        training_index = math.floor(training_ratio * len(data))
        training = data[0:training_index]
        testing = data[training_index:]
        return training, testing

    def yes_and_no_counters(self, data) -> None:

        # First is for YES and second is for NO
        for i in range(len(data[0])):
            self.counters.append([0, 0])

        for row in data:
            for i in range(len(row)):
                if i == 0:
                    continue
                else:
                    if row[i] == 'y':
                        self.counters[i][0] += 1
                    elif row[i] == 'n':
                        self.counters[i][1] += 1


    def assume_missing_values(self, data) -> 'the data after filling missing values':

        self.yes_and_no_counters(data)

        for row in data:
            for i in range(len(row)):
                if i == 0:
                    continue
                else:
                    if row[i] == '?':
                        row[i] = 'y' if self.counters[i][0] > self.counters[i][1] else 'n'
