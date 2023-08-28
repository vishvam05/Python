try:
    a=int(input("enter a : "))
    b=int(input("enter b : "))
    c=a/b
    print("a/b=%d"%c)
except Exception:
    print("can't divide by 0")
else:
    print("Fn is working ok")