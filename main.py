# fileref = open("ccdata.txt", "r")


# print(fileref.read())
# fileref.close()
ccfile = open("ccdata.txt", "r")

for aline in ccfile:
    values = aline.split()
    for val in len(values):
        if val > 1:
            print("len bigger than 1")
        else:
            print("not bigger than")
    # print(len(values))
    # print(values)

ccfile.close()