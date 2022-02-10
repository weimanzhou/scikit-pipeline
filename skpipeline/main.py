import pandas as pd
import pdpipe as pdp
from pdpipe import MapColVals, ApplyToRows, OneHotEncode, ColDrop
from sklearn.pipeline import Pipeline

from src.pdpipe import *

# plt.switch_backend('TkAgg')
# !kaggle competitions download -c titanic

df_train = pd.read_csv(r'E:\GITHUB\iml\src\dataset\titanic\train.csv')
df_test = pd.read_csv(r'E:\GITHUB\iml\src\dataset\titanic\test.csv')

columns = df_test.columns

X = df_train.copy()
y = df_train['Survived']

X = pd.concat([df_train, df_test])

pipe = Pipeline([
    # 理解数据
    ('understand_data', InfoData()),
    # ('drop_col[name]', pdp.ColDrop('Name')),
    # 绘制相关图形
    # ('plot_bar', PlotBar(columns=['Embarked', 'Parch', 'SibSp', 'Pclass', 'Sex'], y='Survived')),
    # ('plot_facet_grid', PlotFacetGrid(columns=['Age', 'Fare'], hue='Survived')),
    # ('plot_dist', PlotDistPlot(columns=['Fare'])),
    # 数据清洗
    ('log_fare', pdp.Log(columns=['Fare'])),
    # ('wrapper_pd', WrapperDF()),
    # 填充数据
    ('fill[Cabin]', pdp.df.fillna(value={'Cabin': 'U', 'Embarked': 'S'})),
    # ('fill_age', FillNa(column='Age')),
    ('understand_data3', InfoData()),
    # ('generate_col_title', ApplyByCols("Name", lambda col: col.split(',')[1].split('.')[0].strip())),
    ('generate[Title]', ApplyToRows(lambda row: row['Name'].split(',')[1].split('.')[0].strip(), 'Title')),
    # ('plot_bar[title]', PlotBar(columns=['Name'], y='Survived')),
    # ('rename_name2title', ColRename({'Name': 'Title'})),
    ('replace', MapColVals("Title", {
        'Mr': 'Mr',
        'Mlle': 'Miss',
        'Miss': 'Miss',
        'Master': 'Master',
        'Jonkheer': 'Master',
        'Mme': 'Mrs',
        'Ms': 'Mrs',
        'Mrs': 'Mrs',
        'Don': 'Royalty',
        'Sir': 'Royalty',
        'the Countess': 'Royalty',
        'Dona': 'Royalty',
        'Lady': 'Royalty',
        'Capt': 'Officer',
        'Col': 'Officer',
        'Major': 'Officer',
        'Dr': 'Officer',
        'Rev': 'Officer'
    })),
    ('plot_bar[title]', PlotBar(columns=['Title'], y='Survived')),
    ('generate[FamilyNum]', ApplyToRows(lambda row: row['Parch'] + row['SibSp'] + 1, 'FamilyNum')),
    ('plot_bar[FamilyNum]', PlotBar(columns=['FamilyNum'], y='Survived')),
    ('FamilyNum', MapColVals(
        "FamilyNum",
        lambda item: 0 if item == 1 else (1 if item >= 2 & item <= 4 else 2))),
    ('plot_bar[FamilyNum2]', PlotBar(columns=['FamilyNum'], y='Survived')),
    ('generate[Deck]', ApplyToRows(lambda row: row['Cabin'][0], 'Deck')),
    ('plot_bar[Deck]', PlotBar(columns=['Deck'], y='Survived')),
    ('map[Ticket2VCount]', Map2ValueCount(columns=['Ticket'])),
    ('plot_bar[Ticket]', PlotBar(columns=['Ticket'], y='Survived')),
    ('generate[Surname]', ApplyToRows(lambda row: row['Name'].split(',')[0].strip(), 'Surname')),
    ('map[Surname2VCount]', Map2ValueCount(columns=['Surname'])),
    ('drop_col', ColDrop(columns=['PassengerId', 'Name', 'Surname', 'Survived'])),
    ('dropna', pdp.df.dropna()),
    ('describe_data3', InfoData()),
    ('onehot_encoder_cat', OneHotEncode()),
    ('onehot_encoder_num', OneHotEncode(columns=['Parch', 'SibSp', 'Pclass', 'FamilyNum'])),
    ('understand_data4', HeadData()),
    # ('model', FeatureUnion([
    #     ('svc', EstimatorTransformer(SVC())),
    #     ('DecisionTreeClassifier', EstimatorTransformer(DecisionTreeClassifier())),
    #     ('RandomForestClassifier', EstimatorTransformer(RandomForestClassifier())),
    #     ('ExtraTreesClassifier', EstimatorTransformer(ExtraTreesClassifier())),
    #     ('GradientBoostingClassifier', EstimatorTransformer(GradientBoostingClassifier())),
    #     ('KNeighborsClassifier', EstimatorTransformer(KNeighborsClassifier())),
    #     ('LogisticRegression', EstimatorTransformer(LogisticRegression())),
    #     ('LinearDiscriminantAnalysis', EstimatorTransformer(LinearDiscriminantAnalysis())),
    # ]))
    # ('null', IdentityTransformer())
    # ('standard_scale_data', StandardScaler()),
    # ('describe_data', DescribeData()),
    # ('make_mi_score', MakeMIScore()),
    # ('plot_pair', PlotPair()),
    # ('concat', pdp.df.concate(df_test)),
    # ('drop_col_name', pdp.ColDrop("name")),
    # ('model', FeatureUnion([
    #     ('lr', EstimatorTransformer(LinearRegression())),
    #     ('ridge', EstimatorTransformer(Ridge()))
    # ]))
], verbose=True)

df = pipe.fit(X, y).transform(X)
# print(df)
