import numpy as np

"""

if Dimensions match then 
reshape(row , col)

"""

arr = np.array([1,2,3,4])

# 1D ---> N Dimenstion
new_arr = arr.reshape(2,2)
print(new_arr)

# ND ----> 1D  
print(arr.ravel())  # Create view
print(arr.flatten()) # Create Copy
