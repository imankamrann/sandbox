# First line
# Second line
# 3rd line 
# 4th line

from rich.console import Console
console = Console()

import time

def printFileLineByLine(f):
    aline = f.readline()
    while aline:    
        console.print(aline)
        aline = f.readline()

# readOnlyFile = open("f1.txt","r")
# printFileLineByLine(readOnlyFile)
# readOnlyFile.close

# console.print("Program is waiting for 5 seconds")
# time.sleep(5)


file4Writing = open("f2.txt","w")
readOnlyFile = open("f1.txt","r")

aline = readOnlyFile.readline()
 
while aline:
    console.print("Processing new line..")    
    items = aline.split()
    for i in items:
        file4Writing.write("I live in: " +'\t'+ i+'\t')
    file4Writing.write("\n")
    aline = readOnlyFile.readline()
    aline = readOnlyFile.readline()

readOnlyFile.close
file4Writing.close





