import math


class DecisionTree:

    def get_best_attr_to_split_on(self, data):
        pass

    def entropy(self, dataset) -> float:
        """
        :param dataset: list
        :return: entropy: float
        """
        democrats_counter, republicans_counter = 0, 0
        for row in dataset:
            if row[0] == 'democrat':
                democrats_counter += 1
            elif row[0] == 'republican':
                republicans_counter += 1

        democrats_prob = democrats_counter / float(len(dataset))
        republicans_prob = republicans_counter / float(len(dataset))

        return -(democrats_prob * math.log(democrats_prob, 2)) - (republicans_prob * math.log(republicans_prob, 2))
