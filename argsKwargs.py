def multiply(*numbers):
    product = 1
    for n in numbers:
        product*=n
    return product

print("product: ", multiply(1,2,3,4,5))

# *args takes multiple arguments in a method instead of a separate variable for each indiv

def makeSentence(**word):
    sentence = ''
    for word in word.values():
        sentence += word
    return sentence

print("sentence: ", makeSentence(a="i ", b="am ", c="marceline "))