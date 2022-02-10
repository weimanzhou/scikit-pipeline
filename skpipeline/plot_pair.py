import matplotlib.pyplot as plt
import seaborn as sns


class PlotPair():

    def fit(self, X, y=None, exraise=None, verbose=False):
        return X

    def transform(self, X, y=None, exraise=None, verbose=False):
        sns.pairplot(X)
        plt.show()
        return X

    def fit_transform(self, X, y=None, exraise=None, verbose=False):
        return X
