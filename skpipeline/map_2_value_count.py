class Map2ValueCount():

    def __init__(self, columns=[]):
        self.columns = columns

    def fit(self, X, y=None, exraise=None, verbose=False):
        return X

    def transform(self, X, y=None, exraise=None, verbose=False):
        for col in self.columns:
            value_count_dict = X[col].value_counts()
            X[col] = X[col].map(value_count_dict)
        return X

    def fit_transform(self, X, y=None, exraise=None, verbose=False):
        return X
