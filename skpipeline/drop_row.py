from abc import ABC


class DropRow(ABC):

    """
    :param condition TODO
    """
    def __init__(self, condition):
        self.condition = condition

    def fit(self, X, y=None, exraise=None, verbose=False):
        return X

    def transform(self, X, y=None, exraise=None, verbose=False):
        pass

    def fit_transform(self, X, y=None, exraise=None, verbose=False):
        return X