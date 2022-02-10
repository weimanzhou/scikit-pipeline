from abc import ABC


class SelRow(ABC):

    def __init__(self, condition):
        self.condition = condition

    def fit(self, X, y=None, exraise=None, verbose=False):
        return X

    def transform(self, X, y=None, exraise=None, verbose=False):
        return X[self.condition]

    def fit_transform(self, X, y=None, exraise=None, verbose=False):
        return X
