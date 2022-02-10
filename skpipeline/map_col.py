from abc import ABC


class MapCol(ABC):

    def __init__(self, columns=None, constant=None, dict=None, function=None):
        self.columns = columns
        self.constant = constant
        self.dict = dict
        self.function = function

    def fit(self, X, y=None, exraise=None, verbose=False):
        return X

    def transform(self, X, y=None, exraise=None, verbose=False):
        if self.constant is not None:
            if len(self.constant) == len(self.columns):
                for col, const in zip(self.columns, self.constant):
                    X[col] = const
            else:
                for col in self.columns:
                    X[col] = self.constant
            return X
        if self.function is not None:
            for col in self.columns:
                X[col] = X[col].map(self.function)
            return X
        if self.dict is not None:
            for col in self.columns:
                X[col] = X[col].map(self.dict)
            return X
        return X

    def fit_transform(self, X, y=None, exraise=None, verbose=False):
        return X