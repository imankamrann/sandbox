petList = ["cat", "dog", "bird"]
longList = []
for i in petList:
    if len(i) == 4:
        print(i, " is 4 char long!!")
        longList.append(i)
        print("\nnew list: ", longList)
    else:
        print(i, " is not 4 char long")



newList = [i for i in petList if len(i)==4]

print(newList)
val = newList[0]
print(val)