#for converting characters to upper case
str1="new york"
str2= str1.upper()
print(str2)


#to lower case
str3=str2.lower()
print(str3)

#for capitalizing 1st character of a string
str4=str3.capitalize()
print(str4)

#for stripping any trailing white space

hello="      hello world     "
print(hello.strip())
print(hello)

#replace old substring with new substring 'count' number of times

world= "welcome to college, this is a beautiful college"
print(world.replace("college", "school"))
print(world.replace("college", "school",1))


#split- split a string into a list of substrings
#by default seperator is " "
#string.split(sep, maxsplit)
s="apple mango banana"
print(s.split())
print(s.split(" ", 1))


#concatenation
print(hello+world)

#format=> to insert variable values in a string
name= "dia"
marks= 97
full= "student name is {x} and marks is {m}".format(x=name, m=marks)
print(full)


