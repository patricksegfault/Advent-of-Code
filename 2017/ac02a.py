import sys

with open(sys.argv[1], 'r') as inFile:
    total = 0
    for line in inFile:
        line = list(map(int, line.strip().split()))
        total += abs(max(line) - min(line))
    print(total)
