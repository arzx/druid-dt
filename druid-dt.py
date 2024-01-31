import numpy as np
import pandas as pd
import seaborn as sns


class Druid:
    def __init__(self, max_depth, min_examples) -> None:
        self.max_depth = max_depth
        self.min_examples = min_examples

    def entropy(self,p, class_probabilities:list):
        return sum([-p_i * np.log2(p_i) for p_i in class_probabilities if p > 0])

    def information_gain(entropy, class_probabilities):
        return entropy() - sum([p * entropy() for p in class_probabilities])

    def gini_index(p):
        return 1 - sum([p_i ** 2 for p_i in p])
    
    def class_probabilities():
        pass

    def data_entropy():
        pass

    def partition_entropy():
        pass

    def split():
        pass

    def find_best_split():
        pass

    def find_label_probabilities():
        pass
    
    def create_tree():
        pass

    def pred_one_sample():
        pass

    def train():
        pass

    def predict_p():
        pass

    def predict():
        pass

    def print_tree():
        pass

    def print_recursive():
        pass
