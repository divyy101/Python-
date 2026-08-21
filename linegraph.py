import matplotlib
import matplotlib.pyplot as plt
import numpy as np
# xpoints=np.array([0,1,2,3])
# ypoints=np.array([0,2,0,2])
# plt.plot(xpoints,ypoints)
# plt.show()
# a=1
# b=2

# x=2
# y=a*x+b
# x=np.array([0,1,2,3,4])
# y=np.array([0,1,0,1,0])
# plt.plot(x,y)
# plt.show()
x=np.array([1,2,3,4])
y=np.array([100,150,75,120])
plt.plot(x,y,'o')
plt.xlabel('month')
plt.ylabel('sales')
plt.title('Data sales')
plt.grid()
plt.show()