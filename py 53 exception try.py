try:
    n=int(input("Enter your age : "))
    if n<18:
        raise ValueError
    else:
      print("Your age is valid... :)")
except ValueError:
  print("Your are not eligible as your age is under 18.  :(")