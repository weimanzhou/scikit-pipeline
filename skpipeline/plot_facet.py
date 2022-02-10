import matplotlib.pyplot as plt
import seaborn as sns


class PlotFacetGrid():
    """
    :param columns:
    :param y:
    """

    def __init__(self, columns, hue):
        self.columns = columns
        self.hue = hue

    def fit(self, X, y=None, exraise=None, verbose=False):
        return X

    def transform(self, X, y=None, exraise=None, verbose=False):
        for col in self.columns:
            # 创建坐标轴
            ageFacet = sns.FacetGrid(X, hue=self.hue, aspect=3)
            # 作图，选择图形类型
            ageFacet.map(sns.kdeplot, col, shade=True)
            # 其他信息：坐标轴范围、标签等
            ageFacet.set(xlim=(0, X[col].max()))
            ageFacet.add_legend()
            plt.savefig('PlotFacetGrid' + col)
            # plt.show()
        return X

    def fit_transform(self, X, y=None, exraise=None, verbose=False):
        return X
