import sys

def partOne(pInput):
    tPossible = 0
    for triangle in pInput:
        allSides = []
        for side in triangle:
            if side == '':
                continue
            allSides.append(int(side))
        allSides.sort()
        if allSides[0] + allSides[1] > allSides[2]:
            tPossible += 1
            
    return tPossible

def partTwo(pInput):
    tPossible = 0
    tGroup = 0
    allSides = []
    
    for triangle in pInput:
        for side in triangle:
            if side == '':
                continue
            allSides.append(int(side))
        tGroup += 1
        if tGroup == 3:
            tGroup = 0
            t1 = [allSides[0], allSides[3], allSides[6]]
            t2 = [allSides[1], allSides[4], allSides[7]]
            t3 = [allSides[2], allSides[5], allSides[8]]
            t1.sort()
            t2.sort()
            t3.sort()
            if t1[0] + t1[1] > t1[2]:
                tPossible += 1
            if t2[0] + t2[1] > t2[2]:
                tPossible += 1
            if t3[0] + t3[1] > t3[2]:
                tPossible += 1
            allSides = []
            
    return tPossible

pInput = ''
with open(sys.argv[1], 'r') as f:
    pInput = f.readlines()
    i = 0
    for p in pInput:
        p = p.strip()
        pInput[i] = p.split(' ')
        i += 1

print("Part One Answer: " + str(partOne(pInput)))
print("Part Two Answer: " + str(partTwo(pInput)))
