
#24 April 24
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#Dataset path on office laptop
#dataset = pd.read_csv(r"C:\Users\joshshr01\Downloads\Data.csv")

#Dataset path on personal laptop
dataset = pd.read_csv("/Users/shreyajoshi/Documents/LEARN/LEARN_ML/Machine Learning A-Z (Codes and Datasets)/Part 1 - Data Preprocessing/Section 2 -------------------- Part 1 - Data Preprocessing --------------------/Python/Data.csv")
dataset
dataset.iloc[:2,:4] #First is row's range. After comma is columns's range.
dataset.iloc[:,:-1] #Rows is before comma, and column is after comma.
#This prints all rows, and all columns except last column.
dataset.iloc[:1,:] #First row of all columns.

x = dataset.iloc[:,:-1].values #Without .values, it will not extract data as numpy arrays.
y = dataset.iloc[:,-1].values
print(x)
print(y)

