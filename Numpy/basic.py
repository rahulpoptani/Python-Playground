import numpy as np

# Creating Array 0D
a = np.array(20)
print(a)

# Creating Array 1D
b = np.array([1,2,3])
print(b)

# Creating Array 2D
c = np.array([[1,2,3], [4,5,6]])
print(c)

# Creating Array 3D
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(d)

# Check dimension
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

####################################################################################################################################

arr = np.array([1, 2, 3, 4])
print(arr.dtype)
arr = np.array(['apple', 'banana', 'cherry'], dtype='S')
print(arr.dtype)

# Change to another type
arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype(int)
print(newarr.dtype)

arr = np.array([0,1,2])
arrnew = arr.astype(bool)
print(arrnew)



arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print(arrnew)



arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print(arr) # [1 2 3 4 5 6]



arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(newarr) 


arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x) 



arr = np.array([3, 2, 0, 1])
print(np.sort(arr)) 


arr = np.array([41, 42, 43, 44])
x = [True, False, True, False]
newarr = arr[x]
print(newarr) 

####################################################################################################################################

