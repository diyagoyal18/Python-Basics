# #  {} brackets used

# unordered
# immutable- > cant remove existing items but can remove or add
# unindexed
# duplication not allowed
# any database
# mix of different datatypes

names={"riya", "diya", "sia"}
print(names)

#accessing items
for x in names:
    print(x)

#add elements
names.add("sia")
print(names)

#add another sequence
name_list =["pia", "tia"]
names.update(name_list)
print(names)

#remove elements
names.remove("tia")
print(names)

#if we dont know that an item is present in set or not but still we want to remove it then we use discard function bcz by using remove function it throws an error

names.discard("diyaa")
print(names)

#join 2 sets

s1={'a','b','c'}
s2={'q','e','c'}
print(s1,s2)
print(s1.union(s2)) #in union duplicate values are not allowed
s1.update(s2)
print(s1)


#keep only duplicates while joining
s1.intersection_update(s2)
print(s1)

#keep all except duplicates
s1.symmetric_difference_update(s2)
print(s1)