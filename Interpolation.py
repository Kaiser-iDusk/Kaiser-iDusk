import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
def spec_product(X, i):
    product = 1
    j = 0
    while j < len(X):
        if j == i:
            pass
        else:
            product *= (X[i] - X[j])
        j+=1
    return product
def piece_product(X, w, i):
    product = 1
    j = 0
    while j < len(X) :
        if j != i:
            product *= (w - X[j])
        j+=1
    return product
X= np.asarray(list(map(float, input("Enter X vals: ").split()))) 
Y= np.asarray(list(map(float, input("Enter Y vals: ").split()))) 
Z= []
# print(list(zip(X, Y)))
for x in range(len(X)):
    Z.append(Y[x]/spec_product(X, x))
print(Z)
print("For extrapolating, input the extrapolation abscissa in the subsequent line:")
w = float(input())
sum = 0
for x in range(len(X)):
    sum += Z[x] * piece_product(X, w, x)
    # print(sum)
print(sum, " is the extrapolated ordinate!")
plt.scatter(x= X, y= Y, c= 'r')
plt.show()