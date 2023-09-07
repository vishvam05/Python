import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
b=np.array([[4,2,7],[9,6,4],[6,4,6]])
print("always vertically concatened\n",np.vstack((a,b)))
print("always vertically concatened\n",np.hstack((a,b)))
