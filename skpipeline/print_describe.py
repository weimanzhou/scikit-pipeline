class DescribeData():

    def fit(self, X, y=None, exraise=None, verbose=False):
        return X

    def transform(self, X, y=None, exraise=None, verbose=False):
        print(X.describe())
        return X

    def fit_transform(self, X, y=None, exraise=None, verbose=False):
        return X
