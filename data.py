import numpy as np
import pandas
import matplotlib.pyplot as plt

def SumSquare(x):
    return np.sum(np.square(x))
def SquareSum(x):
    return np.square(np.sum(x))
def SumProd(x,y):
    return np.sum(x*y)


a0 = lambda x, y: ((SumSquare(x) * np.sum(y) - np.sum(x) * SumProd(x,y)) / (len(x) * SumSquare(x) - SquareSum(x)))
a1 = lambda x, y: ((len(x) * SumProd(x,y) - np.sum(x)*np.sum(y))/(len(x)*SumSquare(x)-SquareSum(x)))

df = pandas.read_excel("DATA.xlsx")
x = np.array(df["X"])
y = np.array(df["Y"])
LnX = np.log(x[1:])
LnY = np.log(y[1:])
print(len(x))

def M(y, fx):
    return np.sum([(y[i] + fx[i]) / 2 for i in range(len(y))]) / len(y)

def D(y, fx):
    return SumSquare([(y[i] + fx[i]) / 2 for i in range(len(y))]) / len(y)

def R(y, fx):
    m = M(y, fx)
    return 1 - SumSquare(y - fx) / SumSquare([y[i] - m for i in range(len(y))])


fig, ax = plt.subplots()
plt.grid()

