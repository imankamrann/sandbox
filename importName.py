#py module
import json
print("hi")
#file = "names.json"

# with open (file, "r") as json_file:
#     data = json.load(json_file)
#     nameData = data["names"]
#     for item in nameData:
#         name = (item["firstname"])
#         age = (item["age"])
#         print(f"{name} is {age}")

# def write_json(data, filename="dumpFile"):
#     with open(filename, "w") as f:
#         json.dump(data, f, indent=4)

# data = ["Bob", "Cindy"]
# write_json(data)

def newPerson(name, age):
 newName = input("enter new name: ")
 newAge = input("enter new age: ")
 return newName, newAge
 

def write_json(data, filename="names.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

with open ("names.json") as json_file:
    data = json.load(json_file)
    userInput = newPerson(name='', age='')
    temp = data["names"]
    y = {"firstname": {userInput.name}, "age": {userInput.age}}
    temp.append(y)

write_json(data)


 

