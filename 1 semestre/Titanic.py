#Leão Pereira
#RA: 22200115
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

pd.options.display.max_columns = None

train = pd.read_csv('/content/sample_data/train.csv')
test = pd.read_csv('/content/sample_data/test.csv')

(train.isnull().sum() / train.shape[0]).sort_values(ascending=False)
train[['Sex', 'Survived']].groupby(['Sex']).mean()
fig, (axis1, axis2, axis3) = plt.subplots(1,3, figsize=(12,4))

sns.barplot(x='Sex', y='Survived', data=train, ax=axis1)
sns.barplot(x='Pclass', y='Survived', data=train, ax=axis2)
sns.barplot(x='Embarked', y='Survived', data=train, ax=axis3);

age_survived = sns.FacetGrid(train, col='Survived')
age_survived.map(sns.distplot, 'Age')

columns=['Parch', 'SibSp', 'Age', 'Pclass']
pd.plotting.scatter_matrix(train[columns], figsize=(15, 10));

sns.heatmap(train.corr(), cmap='coolwarm', fmt='.2f', linewidths=0.1,
            vmax=1.0, square=True, linecolor='white', annot=True);

train.describe(include=['O'])

train_idx = train.shape[0]
test_idx = test.shape[0]

passengerId = test['PassengerId']

target = train.Survived.copy()
train.drop(['Survived'], axis=1, inplace=True)

df_merged = pd.concat(objs=[train, test], axis=0).reset_index(drop=True)

print("df_merged.shape: ({} x {})".format(df_merged.shape[0], df_merged.shape[1]))

df_merged.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1, inplace=True)

df_merged.isnull().sum()

age_median = df_merged['Age'].median()
df_merged['Age'].fillna(age_median, inplace=True)

fare_median = df_merged['Fare'].median()
df_merged['Fare'].fillna(fare_median, inplace=True)

embarked_top = df_merged['Embarked'].value_counts()[0]
df_merged['Embarked'].fillna(embarked_top, inplace=True)

df_merged['Sex'] = df_merged['Sex'].map({'male': 0, 'female': 1})

embarked_dummies = pd.get_dummies(df_merged['Embarked'], prefix='Embarked')
df_merged = pd.concat([df_merged, embarked_dummies], axis=1)
df_merged.drop('Embarked', axis=1, inplace=True)

display(df_merged.head())

train = df_merged.iloc[:train_idx]
test = df_merged.iloc[train_idx:]

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

lr_model = LogisticRegression(solver='liblinear')
lr_model.fit(train, target)

acc_logReg = round(lr_model.score(train, target) * 100, 2)
print("Acurácia do modelo de Regressão Logística: {}".format(acc_logReg))

y_pred_lr = lr_model.predict(test)

submission = pd.DataFrame({
    "PassengerId": passengerId,
    "Survived": y_pred_lr
})

submission.to_csv('./submission_lr.csv', index=False)

tree_model = DecisionTreeClassifier(max_depth=3)
tree_model.fit(train, target)

acc_tree = round(tree_model.score(train, target) * 100, 2)
print("Acurácia do modelo de Árvore de Decisão: {}".format(acc_tree))

y_pred_tree = tree_model.predict(test)

submission = pd.DataFrame({
    "PassengerId": passengerId,
    "Survived": y_pred_tree
})

submission.to_csv('./submission_tree.csv', index=False)

Lion = np.array([2, 0, 35, 1, 1, 32.2, 0, 0, 0, 1]).reshape((1, -1))
Breatrice = np.array([2, 1, 30, 0, 1, 32.2, 0, 0, 0, 1]).reshape((1, -1))

print("Lion:\t{}".format(tree_model.predict(Lion)[0]))
print("Beatrice:\t{}".format(tree_model.predict(Breatrice)[0]))