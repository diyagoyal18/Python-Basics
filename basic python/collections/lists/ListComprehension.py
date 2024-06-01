# list comprehension

# when we want to make a new list from items from the existing list

fruits = ["apple", "mango", "cherry"]
new_fruits=[fruit for fruit in fruits if "a" in fruit]
print(new_fruits)

#copy a list
new_fruits= fruits.copy()
print(new_fruits)

#concatenation of lists
new_fruits= fruits + new_fruits
print(new_fruits)

