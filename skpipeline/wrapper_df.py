import pandas as pd


class WrapperDF():

    def fit(self, X, y=None, exraise=None, verbose=False):
        return X

    def transform(self, X, y=None, exraise=None, verbose=False):
        X = pd.DataFrame(X) if type(X) is np.ndarray else X
        print(X.head())
        return X

    def fit_transform(self, X, y=None, exraise=None, verbose=False):
        return X
