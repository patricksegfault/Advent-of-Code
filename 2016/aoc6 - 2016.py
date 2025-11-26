import sys
import collections

def partOne(pInput):
    rotated = zip(*pInput[::-1])
    word = ''
    for w in rotated:
        word += collections.Counter(w).most_common(1)[0][0]
    
    return word

def partTwo(pInput):
    rotated = zip(*pInput[::-1])
    word = ''
    for w in rotated:
        word += collections.Counter(w).most_common()[-1][0]
    
    return word

pInput = []
with open(sys.argv[1], 'r') as fp:
   for line in fp:
       pInput.append(line.strip())

print("Part One Answer: " + str(partOne(pInput)))
print("Part Two Answer: " + str(partTwo(pInput)))
