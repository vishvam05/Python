import numpy as np
a=np.array([[1,2,3],[9,7,8],[4,5,6]])

print("sorting the list")
print(np.sort(a))

print("sorting the rows")
print(np.sort(a,0))

data_type=np.dtype([('name','S10'),('marks',int)])

arr=np.array([('mukesh',200),('john',345)],dtype=data_type)
print("sorting dta ordered by name")
print(np.sort(arr,order='name'))