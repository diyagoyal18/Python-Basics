#nested list


fruits = ["apple", "mango", "cherry"]

fruits.insert(2,["kiwi", "papaya"])
print(fruits)
#['apple', 'mango', ['kiwi', 'papaya'], 'cherry']


#to access kiwi
print(fruits[2][0])