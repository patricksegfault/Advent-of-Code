import sys

with open(sys.argv[1], 'r') as inFile:
    totalValid = 0
    for line in inFile:
        line = line.strip().split()
        if len(line) == len(set(line)):
            totalValid += 1

print(totalValid)
