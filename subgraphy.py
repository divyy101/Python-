# import matplotlib.pyplot as plt
# import numpy as np

# x = np.array([1, 2, 3, 4])
# y = np.array([100, 150, 75, 120])

# plt.subplot(2, 1, 1)
# plt.plot(x, y, 'o-')
# plt.title("Main Graph")
# plt.grid()

# plt.subplot(2, 1, 2)
# plt.plot(x, y, 'o-')
# plt.title("Small Graph")
# plt.grid()

# plt.show()
import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4])
y = np.array([100, 150, 75, 120])

plt.bar(x, y)        # Bar graph
plt.plot(x, y, 'o-') # Line graph

plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Sales Data")
plt.grid()

plt.show()