
#without any arguments
def printhello():
    print("hello")


printhello()


#with arguments
def add(n1,n2):
    sum= n1+n2
    return sum

x=2
y=3
print("sum is ", add(x,y))

#key value pairs
def studentInfo(**kwargs):
    for x,y in kwargs.items():
        print(x,"is",y)

studentInfo(name= "risa", age=32)
studentInfo(name= "diya", age=12)