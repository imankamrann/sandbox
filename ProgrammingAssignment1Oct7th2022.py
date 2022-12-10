from logging.config import valid_ident

p = 2
y = 3
z = 4

value = [p, y, z]

largest_number = value[0]

for x in value:
    if x > largest_number:
        largest_number = x

print("largest number: ", largest_number)




