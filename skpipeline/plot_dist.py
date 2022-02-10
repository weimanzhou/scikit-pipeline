import matplotlib.pyplot as plt
import seaborn as sns


class PlotDistPlot():
    """
    :param columns:
    :param y:
    """

    def __init__(self, columns):
        self.columns = columns if type(columns) == list else [columns]

    def fit(self, X, y=None, exraise=None, verbose=False):
        return X

    def transform(self, X, y=None, exraise=None, verbose=False):
        for col in self.columns:
            sns.histplot(X[col][X[col].notna()], label='skewness: {:.2f}'.format(X[col].skew()))
            plt.savefig('PlotDistPlot' + col)
        return X

    def fit_transform(self, X, y=None, exraise=None, verbose=False):
        return X
