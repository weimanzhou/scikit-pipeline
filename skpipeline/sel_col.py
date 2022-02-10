from abc import ABC


class SelCol(ABC):

    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None, exraise=None, verbose=False):
        return X

    def transform(self, X, y=None, exraise=None, verbose=False):
        return X[self.columns]

    def fit_transform(self, X, y=None, exraise=None, verbose=False):
        return X
