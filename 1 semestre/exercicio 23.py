from gettext import install
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
df = pd.read_excel("train.xlsx", index_col=0)
sns.set_style("white")
plt.figure(figsize=(10, 10))

g = sns.scatterplot(x="Passengerld", y="Pclass", data=df)
plt.show
