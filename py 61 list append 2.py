list=[1,2,3,4,5]
print("Orignal list :")
for i in list:
    print(i,end=" ")
list2=[6,7,8]
list.append(list2)
print("\nList after append of list 1 and list 2")
print(list,end=" ")
list2.append([9,10])
print("\nList after adding some elements in list 2 ")
print(list,end=" ")