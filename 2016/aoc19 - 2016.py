import sys

def partOne(pInput):
    return 2*(pInput - 2**(pInput.bit_length() - 1)) + 1

def partTwo(pInput):
    return 'err'

with open(sys.argv[1], 'r') as f:
    pInput = int(f.readlines()[0])

print("Part One Answer: " + str(partOne(pInput)))
print("Part Two Answer: " + str(partTwo(pInput)))
