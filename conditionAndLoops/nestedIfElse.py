n1=int(input("enter 1st number"))
n2=int(input("enter 2nd number"))
n3=int(input("enter 3rd number"))

if n1>n2:
    if n1>n3:
        print(n1,"is the largest number")
    else:
        print(n3, " is the largest number")
else:
    if n2>n3:
        print(n2, "is the largest number")
    else:
       print(n3, " is the largest number")
