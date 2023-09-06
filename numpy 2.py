import numpy as np
a=np.array([[1,2,3],[5,6,7],[8,9,0]])
b=a.flatten('C')
print(b)
