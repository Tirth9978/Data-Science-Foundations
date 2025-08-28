import numpy as np

"""
np.delete(array , index , axis)

"""

# 1D Array 
arr = np.array([1,2,3,4,5,6,7,8])

new_arr = np.delete(arr,4)
print(new_arr)

# 2D Array 

arr = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])
new_arr = np.delete(arr , 1 , axis=0)
print(new_arr)