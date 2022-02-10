from abc import ABC


class DropCol(ABC):

    """
    :param columns: columns that will be dropped
    """
    def __init__(self, columns=None):
        self.columns = columns

    def fit(self, X, y=None, exraise=None, verbose=False):
        return X

    def transform(self, X, y=None, exraise=None, verbose=False):
        return X.drop(self.columns, axis=1)

    def fit_transform(self, X, y=None, exraise=None, verbose=False):
        return X