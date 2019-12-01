import math


def label_split(dataset):
    yes_counter, no_counter = 0, 0
    for row in dataset:
        if row[0] == 'democrat':
            yes_counter += 1
        elif row[0] == 'republican':
            no_counter += 1
    return yes_counter, no_counter


class DecisionNode:
    decision_attribute = None
    left_subset = []
    right_subset = []

    def __init__(self, decision_attr, left_subset, right_subset):
        self.decision_attribute = decision_attr
        self.left_subset = left_subset
        self.right_subset = right_subset


class Leaf:
    original_dataset_size = 0
    democrats_percent = 0
    republicans_percent = 0

    def __init__(self, dataset):
        self.democrats_predictions, self.republicans_predictions = label_split(dataset)

    def calc_percentages(self, original_dataset_size):
        self.original_dataset_size = original_dataset_size
        self.democrats_percent = round(self.democrats_predictions / float(self.original_dataset_size) * 100, 2)
        self.republicans_percent = round(self.republicans_predictions / float(self.original_dataset_size) * 100, 2)

    def str(self) -> str:
        whole_str = ""
        if self.democrats_predictions != 0:
            whole_str += "democrats: " + str(self.democrats_predictions)
        if self.republicans_predictions != 0:
            whole_str += "republicans: " + str(self.republicans_predictions)
        return whole_str

    def str_with_probability(self) -> str:
        whole_str = ""
        if self.democrats_predictions != 0:
            whole_str += "democrats: " + str(self.democrats_percent) + "% "
        if self.republicans_predictions != 0:
            whole_str += "republicans: " + str(self.republicans_percent) + "%"

        return whole_str


class DecisionTree:
    root = None

    def entropy(self, dataset) -> float:
        """
        :param dataset: list
        :return: entropy: float
        """
        democrats_counter, republicans_counter = label_split(dataset)
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

    def get_best_attr_to_split_on(self, data, attributes_number) -> 'integer, float':
        best_attribute = 1  # best attribute number and its gain
        best_gain = 0
        for i in range(1, attributes_number + 1):
            true_subset, false_subset = self.attribute_split(data, i)

            # Skip this split if it does not divide the dataset
            if len(true_subset) == 0 or len(false_subset) == 0:
                continue

            if self.information_gain(data, i) > best_gain:
                best_attribute = i
                best_gain = self.information_gain(data, i)

        return best_attribute, best_gain

    def build(self, dataset):
        attributes_number = len(dataset[0]) - 1
        # Will return attribute number and corresponding gain
        A, gain = self.get_best_attr_to_split_on(dataset, attributes_number)

        if gain == 0:
            return Leaf(dataset)

        true_subset, false_subset = self.attribute_split(dataset, A)

        true_branch = self.build(true_subset)
        false_branch = self.build(false_subset)
        self.root = DecisionNode(A, true_branch, false_branch)
        return self.root

    def print_tree(self, node, spacing=""):
        # Base case
        if isinstance(node, Leaf):
            whole_str = spacing + "Predict "
            whole_str += node.str()
            print(whole_str)
            return

        print(spacing + "Feature:", node.decision_attribute, "?")

        # Call recursively on the true and false branches
        print(spacing + "--> True")
        self.print_tree(node.left_subset, spacing + " ")
        print(spacing + "--> False")
        self.print_tree(node.right_subset, spacing + " ")

    def print(self):
        self.print_tree(self.root)

    def classify(self, row, node):
        # Base case: we've reached a leaf
        if isinstance(node, Leaf):
            return node

        # Decide whether to follow the true branch or the false branch
        # Compare the feature stored in the node to example we're considering
        if row[node.decision_attribute] == 'y':
            return self.classify(row, node.left_subset)
        else:
            return self.classify(row, node.right_subset)
