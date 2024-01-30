import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
file = pd.read_csv("data_02/iris.csv")



coloumn_names =  ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
#file2 = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", header= None,names=coloumn_names)


#x='5'
#y = 6
#print(y+x)
b ='12.2'
print(b)

val = 2+3*(36/9+1)**2-1
print(val)

y = [0,1,2,3,4,5,6,7,8,9,10]
x = [0,1,2,3,4,5,6,7,8,9,10]

plt.plot(x,y)
plt.show()
