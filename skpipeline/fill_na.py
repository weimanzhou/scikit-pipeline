from abc import ABC

from sklearn.impute import KNNImputer


class FillNa(ABC):
    def __init__(self, condition={}, column=None, value=None, imputer=KNNImputer(n_neighbors=10)):
        self.condition = condition
        self.column = column
        self.value = value
        self.imputer = imputer

    def fit(self, X, y=None, exraise=None, verbose=False):
        X[self.column] = self.imputer.fit(X[self.column])
        return X

    def transform(self, X, y=None, exraise=None, verbose=False):
        X[self.column] = self.imputer.transform(X[self.column])
        return X

    def fit_transform(self, X, y=None, exraise=None, verbose=False):
        X[self.column] = self.imputer.fit_transform(X[self.column])
        return X


if __name__ == '__main__':
    fn = FillNa(column=['B'])
    import pandas as pd
    """
    >>> df = pd.DataFrame({'A': ['a', 'b', 'c'], 'B': [1, None, None]})
    >>> df 
       A    B
    0  a  1.0
    1  b  None
    2  c  None
    >>> df_new = fn.fit_transform(df)
    >>> df_new 
       A    B
    0  a  1.0
    1  b  1.0
    2  c  1.0
    """
    df = pd.DataFrame({'A': ['a', 'b', 'c'], 'B': [1, None, None]})
    df_new = fn.fit_transform(df)
    print(df_new.head())
