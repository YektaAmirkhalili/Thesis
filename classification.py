# how many of each class are there 

import pandas as pd 
import numpy as np 

data = pd.read_csv('dataclassification.csv')
classes = data['class'] #pandas series 
classes_np = classes.values #numpy array 

#count how many 0s and 1s and 2s are there: total amount must equal size of array 
print("number of class A: ", np.sum(classes_np == 1, axis=0)) #class A is 1 
#number of class A:  11

print("number of class B: ", np.sum(classes_np == 2, axis=0)) #class B is 2 
#number of class B: 280

print("number of class C: ", np.sum(classes_np == 0, axis=0)) #class C is 0 
#number of class C: 4110 




