class InfoData():

    def fit(self, X, y=None, exraise=None, verbose=False):
        return X

    def transform(self, X, y=None, exraise=None, verbose=False):
        print(X.info())
        return X

    def fit_transform(self, X, y=None, exraise=None, verbose=False):
        return X
