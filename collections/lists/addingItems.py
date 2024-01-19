# # adding items to a list
#     append()
#     insert()
#     extend()

fruits = ["apple", "mango", "cherry"]

fruits.append("kiwi")
print(fruits)

fruits.insert(2,"banana")
print(fruits)

more_fruits= ["blueberry"]
fruits.extend(more_fruits)
print(fruits)