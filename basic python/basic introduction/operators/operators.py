# operators
#     arithmetic operators    
#         // floor division -> #returns nearest whole number
#         ** exponentiation
# # baaki operators are generic


print("sum: ", 3+4)
print("difference", 4-2)
print("product", 4*2)
print("remainder", 5%2)
print("division", 4/2)
print("floor division", 5//2)
print("exponential", 4**2)


    # assignment operators
    #     = += -= *= /= %= //= **= &= |= ^= >>= <<=

n1=3
n2=n1
n2 += n1
print(n1,n2)

    # comparison operators
    # ==   !=  >   <   <=  >=
    # output is always boolean

n3=6
n4=5
print(n3>n4)


#    logical operators
#     and     or      not

e1= 2>1
e2=5<4
print("e2 and e2", e1 and e2)
print("e1 or e2", e1 or e2)
print("e1 not", not(e1))

        # identity operators
        # is      is not
        # #to check if the variables are the same object

x=4
y=5
print("if x is y", x is y)
print("if x is not y", x is not y)

        # membership operators
        # in      not in
        # to check if the sequence with the specified value is present

fruits = ["apple", "banana", "guava"]
print("if apple is present in fruits", "apple" in fruits)

        # bitwise operators
        # &    ^    ~    >>     <<    |

a=334543
b=4
print("a&b",a&b)
print("a|b",a|b)
print("a^b",a^b)
print("a>>b",a>>b)

#         operators precedence 
# ()
# **
# /,//  
# *
# +,-  
# bitwise shift
# &, |, ^
# comparison
# logical