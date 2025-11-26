import sys
import re

def day12a():
    with open(sys.argv[1]) as f:
        data = f.readlines()
        negNumReg = re.compile('-[0-9]+')
        posNumReg = re.compile('[0-9]+')
        negNums = negNumReg.findall(data[0])
        posNums = posNumReg.findall(data[0])
        negNums = list(map(int, negNums))
        posNums = list(map(int, posNums))
        total = 0
        total += sum(posNums)
        total += sum(negNums)
        total += sum(negNums)

        print (total)

def day12b():
    with open(sys.argv[1]) as f:
        data = f.readlines()

        print("")

day12a()
day12b()
