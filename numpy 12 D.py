import numpy as np
a1=np.array([[1,2,3],[4,5,6],[6,7,8]],ndmin=3)
a2=np.array([[9,8,7],[6,5,4],[3,2,1]],ndmin=3)
result=np.dot(a1,a2)
print(result)
