# This is most important in the ML

import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10])

print(arr[arr > 3])  # Print those elemetns which are bigger then 3

print(arr[arr % 2 != 0]) # Print odd elements
print(arr[arr % 2 == 0]) # Print even Elemetns
