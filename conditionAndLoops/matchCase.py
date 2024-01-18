#calculator 
n1= int(input("enter number 1: "))
n2= int(input("enter number 2: "))

operator= input("enter operator: ")

match operator:
    case "+":
        print("sum is", n1+n2)
    case "-":
        print("difference is", n1-n2)
    case "*":
        print("product is", n1*n2)
    case "/":
        print("divide is", n1/n2)
    case _ :
        print("enter valid operator")
   