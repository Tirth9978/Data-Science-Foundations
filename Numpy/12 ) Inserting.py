import numpy as np 

"""
np.indert(array , inedx , value , axis)

-> array : Our Array 
-> Index : Where you want to insert 
-> value : Value which you want to insert 
-> axis = 0 ---> row-wise 
-> axis = 1 ---> col-wise 

"""

# 1D Array 
arr = np.array([1,2,3,4,5,6,7,8,9])

new_arr = np.insert(arr , 3 , 9978)
print(new_arr)

# 2D Array 

arr = np.array([[1,2,3],[4,5,6]])

# Inserting row
new_arr = np.insert(arr , 1 , [7,8,9] , axis=0)
print(new_arr)

# Inserting Col 
new_arr = np.insert(arr, 1 , [10,12] , axis = 1)
print(new_arr)

# Inserting fattern version 
new_arr = np.insert(arr, 1 , [10,12] , axis = None)
print(new_arr)
