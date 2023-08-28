try:
    a=int(input("Enter 1st value : "))
    b=int(input("Enter 2nd value : "))
    c=a/b
    if b is 0:
        raise ArithmeticError
    else:
        print(a,"/",b,"=%d"%c)
except ArithmeticError:
    print("value can't be 0")