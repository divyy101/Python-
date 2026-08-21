import numpy as np
matrix1=np.array([[1,2,3,4],[5,6,7,8],[3,6,7,9]])
print(matrix1)
n=np.sum(matrix1)
print(n)
for i in matrix1:
    c=0
    for j in i:
        c=c+j
    print(c)
print(np.max(matrix1))
print(np.min(matrix1))
matix2=matrix1.T
print(matix2)

mat3=np.nditer(matrix1)
for x in mat3:
    print(x)
#function for traversal
a=3
b=5
# c=np.bitwise_and(a,b)
# print(c)
# d=np.bitwise_or(a,b)
# print(d)
# a3=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
# print(a3)
m2 = np.array([[1,2,3,4],[5,6,7,8],[1,2,6,8]])
print(m2)
print(id(m2))
cm2 = m2
print(cm2)
print(id(cm2))