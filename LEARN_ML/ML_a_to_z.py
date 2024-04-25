import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dataset = pd.read_csv("/Users/shreyajoshi/Documents/LEARN/LEARN_ML/Machine Learning A-Z (Codes and Datasets)/Part 1 - Data Preprocessing/Section 2 -------------------- Part 1 - Data Preprocessing --------------------/Python/Data.csv")
dataset
dataset.iloc[:2,:4] #First is row's range. After comma is columns's range.
dataset.iloc[:,:-1] #All columns excelpt the last one.
dataset.iloc[:1,:] #First row of all columns.

x = dataset.iloc[:,:-1].values #Without .values, it will not extract data as numpy arrays.
y = dataset.iloc[:,-1].values
print(x)
print(y)

