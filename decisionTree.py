import math


class Node:
    decision_attribute = None
    dataset = []
    left_subset = []
    right_subset = []

    def __init__(self, decision_attr, dataset, left_subset, right_subset):
        self.decision_attribute = decision_attr
        self.dataset = dataset
        self.left_subset = left_subset
        self.right_subset = right_subset


class DecisionTree:

    def label_split(self, dataset):
        yes_counter, no_counter = 0, 0
        for row in dataset:
            if row[0] == 'democrat':
                yes_counter += 1
            elif row[0] == 'republican':
                no_counter += 1
        return yes_counter, no_counter

    def entropy(self, dataset) -> float:
        """
        :param dataset: list
        :return: entropy: float
        """
        democrats_counter, republicans_counter = self.label_split(dataset)
        dataset_len = float(len(dataset))
        democrats_prob = democrats_counter / dataset_len
        republicans_prob = republicans_counter / dataset_len
        return -(democrats_prob * math.log(democrats_prob if democrats_prob > 0 else 1, 2)) - (
                republicans_prob * math.log(republicans_prob if republicans_prob > 0 else 1, 2))

    def attribute_split(self, subset, attribute):
        """
        :param subset: list
        :param attribute: 1 <= int <= 16 (in our example)
        :return:
        """
        yes_subset, no_subset = [], []
        for row in subset:
            if row[attribute] == 'y':
                yes_subset.append(row)
            elif row[attribute] == 'n':
                no_subset.append(row)
        return yes_subset, no_subset

    def information_gain(self, subset, attribute):
        """
        :param subset: list
        :param attribute:  1 <= int <= 16 (in our example)
        each attribute has only yes or no values
        :return:
        """

        H = self.entropy(subset)

        yes_subset, no_subset = self.attribute_split(subset, attribute)

        return H - (len(yes_subset) / float(len(subset)) * self.entropy(yes_subset)) - (
                len(no_subset) / float(len(subset)) * self.entropy(no_subset))

    def get_best_attr_to_split_on(self, data, attributes_number) -> int:
        best_attribute = 1  # best attribute number and its gain
        best_gain = 0
        for i in range(1, attributes_number + 1):
            if self.information_gain(data, i) > best_gain:
                best_attribute = i
                best_gain = self.information_gain(data, i)

        return best_attribute

    def build(self, dataset):
        pass
