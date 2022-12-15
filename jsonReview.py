import json

# readFile = open("10Person.json", 'r') #deserialization

# #writeFile = ("10Person.json", 'w') #serialization


# #read file
# aline = readFile.readline()

# for val in aline:
#     name = val["name"]
#     age = val["age"]
#     print("name of person: ", name)
#     print("age of peson: ", age)
#     aline = readFile.readline()

# readFile.close()
# print("out of for loop!")

#reading a file:

filename = "10Person.json"
with open(filename, 'r') as f:
    values = json.load(f)

for i in values:
    name = i["name"]
    age = i["age"]
    print("\n")
    print("name of person: ", name)
    print("age of person: ", age)
    print("\n")


#writing file:


for i in values:
    n = "your mom"
    i["name"] = n
    
    a = 69
    i["age"] = a
    print("name of person: ")
    print("age of peson: ")
    data = i

with open(filename, 'w') as f:
    json.dump(data, age, f, indent = 4)





    

