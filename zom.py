import pandas as pd
import numpy as np

dataset = pd.read_csv('zomato.csv')
dataset.head()
dataset.info()

dataset.isnull().sum()
dataset['Votes'] = dataset['Votes'].fillna(dataset['Votes'].mean())

dataset.loc[16,"Votes"]=np.nan
print(dataset)
print("check missing values:\n",dataset.isna())
print("count missing values:\n",dataset.isna().sum())
dataset["Votes"].fillna(dataset["Votes"].mean(),inplace=True)
print("after filling missing values:\n",dataset)

sorted_dataset=dataset.sort_values(by="Aggregate rating") 
print(sorted_dataset)

avg_result=dataset.groupby("Cuisines")["Aggregate rating"].mean() 
print("Average Rating Of Cuisines:\n",avg_result)
