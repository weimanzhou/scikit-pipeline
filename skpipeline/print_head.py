class HeadData():

    def fit(self, X, y=None, exraise=None, verbose=False):
        return X

    def transform(self, X, y=None, exraise=None, verbose=False):
        print(X.head())
        return X

    def fit_transform(self, X, y=None, exraise=None, verbose=False):
        return X

