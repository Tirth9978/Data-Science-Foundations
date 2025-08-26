import numpy as np

"""
arr[start : end : step]

-> By dafault step is 1
-> If step -1 then it will print array subset in the reverse order 
-> End is execluded 

arr[start : end]  --> Start to end-1.
arr[ : end] --> 0 to end-1
arr[start : ] -->start to last index    
arr[ : ] --> Whole Array
 
"""

arr = np.array([1,2,3,4,5,6,7,8,9])

print(arr[2 : 5])
print(arr[ :  : -1])





