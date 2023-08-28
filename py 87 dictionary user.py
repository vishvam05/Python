emp={}
n=int(input("enter how many elements you want to enter :  "))
for i in range(n):
    key=input("enter the number : ")
    name=input("enter thr name : ")
    emp.update({key:name})
print(emp)