try:
    a=int(input("enter the value : "))
    b=int(input("enter the value to be divided : "))
    c=a/b
    print(a,"/",b,"=%d"%c)
except:
    print("can't divide by 0")
else:
    print("programme is working fine ;)")