import matplotlib.pyplot as plt 
import pandas as pd 
from sklearn import tree
import seaborn as sns


df=pd.read_csv("C:/Projects/Mall_Customer_SegmentatioData/Mall_Customers.csv")
df=df.drop('CustomerID',axis=1)
print(df)
sns.pairplot(df,hue='Gender',markers='o')

plt.show()