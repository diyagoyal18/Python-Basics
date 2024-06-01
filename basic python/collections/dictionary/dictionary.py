# #dictionary

# ordered
# changeable
# unindexed
# duplicate not allowed (for keys)
# any datatype


phones={
    "john": 353652,
    "ria": 345834,
    "garima": 345342
}
print(phones)
print(type(phones))

#access items in a dictionary
print(phones["john"])
#or
print(phones.get("john"))

print(phones.keys())

phones["john"]=567654
print(phones)

phones["kia"]=35465432
print(phones)

more_phones={
    "rita":5465432
}
phones.update(more_phones)
print(phones)

phones.pop("john")
print(phones)


phones.popitem() #last item will be deleted
print(phones)

for x in phones:
    print(x)
    print(phones[x])


for x,y in phones.items():
    print(x,y)


#nested dictionary
areas= {
    "area1":{
        "x":2,
        "y":3
    },
    "area2":{
        "a":3,
        "b":4
    }
}    
print(areas)
print(areas["area1"]["y"])



# phones.clear()
# print(phones)