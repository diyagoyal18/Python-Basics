# # () brackets used
# they are ordered
# immutable
# duplication allowed
# any database
# mix of different datatypes


colours= ("red", "black", "orange")


#creating tuple for 1 item 
fruits=("apple",)
#or
fruits= tuple(("apple"))


#type of tuple
print(type(colours))

#length  of tuple
print(len(fruits))


#unpacking in a tuple
c1,c2,c3= colours
print(c1,c2,c3)