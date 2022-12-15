import csv

filename = "climateinfo.txt"

with open (filename) as f:
    info = csv.reader(f,delimiter=',')

    # for val in info:
    #     print(val)
    
    for val in info:
        newlist = info.split(',')
        print(newlist)
        
