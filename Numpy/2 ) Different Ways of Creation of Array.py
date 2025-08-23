import numpy as np

# All elements are zeros
arr0 = np.zeros(2)
print(arr0)
arr0 = np.zeros((2,4)) # 2 x 4 Matrix with all elemts zeros
print(arr0)

# All elements are ones
arr1 = np.ones(2)
print(arr1)


# With perticular value 
arr = np.full((2,5),9978)
print(arr)