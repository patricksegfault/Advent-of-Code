import sys

def partOne(inp):
    directsIndex = 0
    x = 0
    y = 0

    for d in inp:
        if d[0] == 'L':
            directsIndex = (directsIndex - 1) % 4
        elif d[0] == 'R':
            directsIndex = (directsIndex + 1) % 4
        else:
            print("ERROR. Neither Left nor Right")
            break

        dist = int(d[1:])
        if directsIndex == 0:
            y += dist
        elif directsIndex == 2:
            y -= dist
        elif directsIndex == 1:
            x += dist
        elif directsIndex == 3:
            x -= dist
        else:
            print("ERROR. Compass broken!")
            break

    return abs(x) + abs(y)

def partTwo(inp):
    directsIndex = 0
    x = 0
    y = 0
    locs = [[0,0]]
    final = -1
    found = False
    
    for d in inp:
        if d[0] == 'L':
            directsIndex = (directsIndex - 1) % 4
        elif d[0] == 'R':
            directsIndex = (directsIndex + 1) % 4
        else:
            print("ERROR. Neither Left nor Right")
            break

        #Horrible way to do this for part 2 (but it DOES work)
        dist = int(d[1:])
        if directsIndex == 0:
            for i in range(dist):
                y += 1
                if [x, y] in locs:
                    final = abs(x) + abs(y)
                    found = True
                    break
                locs.append([x, y])
        elif directsIndex == 2:
            for i in range(dist):
                y -= 1
                if [x, y] in locs:
                    final = abs(x) + abs(y)
                    found = True
                    break
                locs.append([x, y])
        elif directsIndex == 1:
            for i in range(dist):
                x += 1
                if [x, y] in locs:
                    final = abs(x) + abs(y)
                    found = True
                    break
                locs.append([x, y])
        elif directsIndex == 3:
            for i in range(dist):
                x -= 1
                if [x, y] in locs:
                    final = abs(x) + abs(y)
                    found = True
                    break
                locs.append([x, y])
        else:
            print("ERROR. Compass broken!")
            break

        if found:
            break

    return final

with open(sys.argv[1], 'r') as f:
    dirInput = f.readlines()[0]
    inp = dirInput.split(', ')

print("Part One Answer: " + str(partOne(inp)))
print("Part Two Answer: " + str(partTwo(inp)))
