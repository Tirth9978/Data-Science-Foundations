import numpy as np 

arr = np.array([1.4,34.5,21.4])

# Before Type casting
print(arr.dtype)

# After Type Casting 
Int_Array = arr.astype(int)
print(Int_Array)
print(Int_Array.dtype)
