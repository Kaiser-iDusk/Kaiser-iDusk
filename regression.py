#idea is to use log transform and 
#perform linear regression to
#determine the bias and slope

#libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#functions for regression
def mew(A):
    sum = 0
    for x in A:
        sum += float(x)
    return sum / len(A)
def cov(A, B):
    sum = 0
    for x in range(len(A)):
        mewA = mew(A)
        mewB = mew(B)
        sum += (float(A[x]) - mewA) * (float(B[x]) - mewB)
    return sum / len(A)
def slope(A, B):
    return cov(A, B) / cov(A, A)
def const(A, B):
    return (mew(B) - (slope(A, B) * mew(A)))

#data
A= np.asarray(list(map(float, input("Enter X vals: ").split()))) 
B= np.asarray(list(map(float, input("Enter Y vals: ").split()))) 

#main
x = float(input("Value to be predicted: "))
print("Slope of log-graph= ", slope(A, B), " and constant of log-graph=", const(A, B))
print("Power = ", const(A, B)+slope(A, B)*x)
final = np.exp(const(A, B)+slope(A, B)*x)
print("Predicted value = ", final)

#plots
P = slope(A, B)*A + const(A, B)
plt.plot(A, B)
plt.plot(A, P)
plt.scatter(A, B, marker="o")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()