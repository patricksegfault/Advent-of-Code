import sys

def day01a():
    with open(sys.argv[1], "r") as file:
        data = file.readlines()
        freq = 0
        for line in data:
            num = int(line)
            freq += num

        print(freq)

def day01b():
    found = False
    freqList = {0:1}
    freq = 0
    while(not found):
        with open(sys.argv[1], "r") as file:
            data = file.readlines()
            for line in data:
                num = int(line)
                freq += num
                if freq in freqList:
                    found = True
                    break
                freqList[freq] = 1
    print(freq)

day01a()
day01b()
