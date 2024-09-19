


# Simple Linear Regression
## Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

## Importing the dataset
dataset = pd.read_csv(r"C:\Users\joshshr01\Downloads\Salary_Data.csv")
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1].values
## Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
x_train,x_test, y_train,y_test = train_test_split(X,y,test_size=0.2, random_state=1)
print(x_train)
print(y_train)
## Training the Simple Linear Regression model on the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression() #creating instance of class
regressor.fit(x_train, y_train) #it trains the model; it's a method of linear regression class
print(x_train)
print(y_train)
## Predicting the Test set results
y_test_pred = regressor.predict(x_test)
y_train_pred = regressor.predict(x_train)
## Visualising the Training set results
print(y_test_pred)
print(y_test)

plt.scatter(x_train,y_train, color = "red")
plt.plot(x_train, y_train_pred, color = 'blue')
plt.title("Salary v/s Exp - Training set")
plt.xlabel("Exp in years")
plt.ylabel("Salary")
plt.show()
## Visualising the Test set results

plt.scatter(x_test, y_test, color = "red")
plt.plot(x_train, y_train_pred, color = 'blue')
plt.title("Salary v/s Exp - Test Set")
plt.xlabel("Exp in years")
plt.ylabel("Salary")
plt.show()
