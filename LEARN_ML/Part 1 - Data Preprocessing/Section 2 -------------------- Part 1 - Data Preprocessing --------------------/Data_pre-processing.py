







#Import the libraries
import numpy as np
import matplotlib.pyplot as plt 
#pyplot is a module in matplotlib library
import pandas as pd
Import the dataset
dataset = pd.read_csv(r"C:\Users\joshshr01\Downloads\Data.csv")
#dataset = pd.read_csv("/Users/shreyajoshi/Documents/LEARN/LEARN_ML/Machine Learning A-Z (Codes and Datasets)/Part 1 - Data Preprocessing/Section 2 -------------------- Part 1 - Data Preprocessing --------------------/Python/Data.csv")
dataset
dataset.info()
dataset.head()
dataset.iloc[:2,:4] #First is row's range. After comma is columns's range.
dataset.iloc[:,:-1] #Rows is before comma, and column is after comma.
#This prints all rows, and all columns except lsat column.
dataset.iloc[:1,:] #First row of all columns.
x = dataset.iloc[:,:-1].values #Without .values, it will not extract data as numpy arrays.
y = dataset.iloc[:,-1].values
print(x)
print(y)
#Finding and handling missing data
missing_data = dataset.isnull().sum() #To check for missing data and it's count
print(missing_data)
from sklearn.impute import SimpleImputer
#Creating an instance of this class 
# Creating an object of a class, here imputer is an object
# Call the class, here SimpleImputer is class with "()"
imputer = SimpleImputer(missing_values=np.nan, strategy="mean")

#apply imputer object on the matrix of features

# Fit method, looks at missing values in the column and compute the average
#To replace, transform method is used.

imputer.fit(x[:,1:3]) #Only select numerical columns, that's why range here is 1:3
x[:,1:3] = imputer.transform(x[:,1:3])

#If you only had numerical data, 
#simply apply the mean transformation to the whole data
# Eg: imputer.fit(dataset)
#Eg: dataset = imputer.transform(dataset)
imputer_mo = SimpleImputer(missing_values=np.nan, strategy="median")
x1=x
imputer.fit(x1[:,1:3]) #Only select numerical columns, that's why range here is 1:3
x[:,1:3] = imputer.transform(x1[:,1:3])
print(x1)

#x1 = dataset.iloc[:,:-1]
#x1 = x1.replace(to_replace = np.nan, value = 9)
#x1
print(x)
print(dataset)
# Encoding categorical data
# one-hot encoding
from sklearn.compose import ColumnTransformer

from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(),[0])], remainder='passthrough' )
x = np.array(ct.fit_transform(x))
x
#Encoding for yes/no
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder() #no is 0 and 1 is yes
y= le.fit_transform(y)
y
dataset
#dataset.drop("Salary", axis=1)
dataset.drop(2) #drops 3rd row, Python Indexes from 0
print(x)
print(y)

df = pd.DataFrame(dataset)
encoded_df = pd.get_dummies(df, columns={"Country"})
encoded_df
print(x)
print(y)
from sklearn.model_selection import train_test_split
x_train,x_test, y_train,y_test = train_test_split(x,y,test_size=0.2, random_state=1)
print(x_train)
print(x_test)
print(y_train)
print(y_test)
#Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train[:,3:] = sc.fit_transform(x_train[:,3:])
x_test[:,3:] = sc.transform(x_test[:,3:])
print(x_train)
print(x_test)
