#!/usr/bin/python3
from datetime import datetime
import os

# search queries
searchQueries = input("\nEnter search queries seperated with spaces, or none to list all\n\n").split()

# current date and time
currentDateTime = datetime.now().strftime('%d/%m/%Y %H:%M')

# read hist file
histPath = os.getcwd() + '/.tempHist'
histListFile = open(histPath, 'r')

# prep printArr
histArr = []

# sort db entries
for line in histListFile:
    if line[0:10].isnumeric():
        ts = int(line[0:10])
        hrTs = datetime.utcfromtimestamp(ts).strftime('%d/%m/%Y %H:%M')
        url = line[17:]
        if len(url) >= 65:
            url = url[0:65] + '\n'

        if len(searchQueries) > 0:
            for id, query in enumerate(searchQueries):
                if line[17:].find(searchQueries[id]) == -1:
                    continue
                elif line[17:].find(searchQueries[id]) > -1:
                    histElement = hrTs + '  -  ' + url
                    histArr.append(histElement)

        else:
            histElement = hrTs + '  -  ' + url
            histArr.append(histElement)



# print db entries
print(f"\nCurrent date and time: {currentDateTime}\n")
for i in histArr:
    print(i, end='')

print(f"\nCount: {len(histArr)}\n")

# close hist file
histListFile.close()
