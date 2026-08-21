import numpy as np


arr = np.array([1, 2, 3, 4, 5])

print("Array:", arr)
print("Sum:", arr.sum())
print("Mean:", arr.mean())
print("max",arr.max())
print("min",arr.min())
array_2d = np.array([[1, 2, 2, 3], [5, 4, 6, 7]])

print("2D Array:\n", array_2d)
print(array_2d.ndim)
for i in arr:
    print(i,end=" ")
print()    
for i in array_2d:
    for j in i:
        print(j,end=" ")
    print()      
