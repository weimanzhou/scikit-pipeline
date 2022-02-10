import matplotlib.pyplot as plt
import seaborn as sns


class PlotBar():
    """
    :param columns:
    :param y:
    """

    def __init__(self, columns, y, doc=True):
        self.columns = columns
        self.y = y
        self.doc = doc

    def fit(self, X, y=None, exraise=None, verbose=False):
        return X

    def transform(self, X, y=None, exraise=None, verbose=False):
        for col in self.columns:
            sns.barplot(data=X, x=col, y=self.y)
            plt.savefig(col)
            # if self.doc is True:
            #
            # plt.show()

        return X

    def fit_transform(self, X, y=None, exraise=None, verbose=False):
        return X
