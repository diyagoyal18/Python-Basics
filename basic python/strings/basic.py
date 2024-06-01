# sequence of characters
# immutable
#indexing

name='college is fun'

name2= "hello  ppl"

name3='''welcome back to 
my channel''' #for multi line string we use ''' '''

print(name, name2, name3)
print(type(name3))

print(name[0])
print(name3[-1])

#traversing a string

for i in name:
    print(i)

#list comprehension
list = [char for char in name]
for i in list:
    print(i)


print(len(name))    

#find character or substring in a string
#find function-> return 1st occurence of the character or substring.. and return -1 when a character is not present
print(name.find('f'))

#slicing
small= name[2:5]
print(small)


