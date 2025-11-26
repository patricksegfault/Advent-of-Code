import sys
import collections
import re

def abba(seq):
    abbaSeq = False
    oldC = ''
    oldC2 = ''
    state = 0
    for c in seq:
        if state == 0:
            oldC = c
            state = 1
        elif state == 1:
            if oldC != c:
                state = 2
                oldC2 = c
        elif state == 2:
            if oldC2 == c:
                state = 3
            else:
                oldC = oldC2
                oldC2 = c
        elif state == 3:
            if oldC == c:
                abbaSeq = True
                break
            elif oldC2 == c:
                state = 1
                oldC = c
            else:
                state = 2
                oldC = oldC2
                oldC2 = c
            
    return abbaSeq

def partOne(pInput):
    count = 0

    for line in pInput:
        addCount = False
        hypernetSeq = False
        for seq in line:
            isAbba = abba(seq)
            
            if isAbba and not hypernetSeq:
                addCount = True
            if isAbba and hypernetSeq:
                addCount = False
                break

            hypernetSeq = not hypernetSeq

        if addCount:
            count += 1
    
    return count

def partTwo(pInput):
    return 'err'

pInput = []
with open(sys.argv[1], 'r') as fp:
   for line in fp:
       pInput.append([field for field in re.split('\\W+', line.strip())])

print("Part One Answer: " + str(partOne(pInput)))
print("Part Two Answer: " + str(partTwo(pInput)))
