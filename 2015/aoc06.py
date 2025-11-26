import sys

def digestLine(line):
    line = line.replace(","," ").split(" ")
    if line[0] == "toggle":
        return "TOGGLE",int(line[1]),int(line[2]),int(line[4]),int(line[5])
    elif line[1] == "on":
        return "ON",int(line[2]),int(line[3]),int(line[5]),int(line[6])
    elif line[1] == "off":
        return "OFF",int(line[2]),int(line[3]),int(line[5]),int(line[6])
    return "ERROR",0,0,0,0

def day6a():
    gridSize = 1000
    lightGrid = [[ 0 for i in range(gridSize) ] for k in range(gridSize) ]
    with open(sys.argv[1], "r") as f:
        lines = f.readlines()

    for line in lines:
        command,startX,startY,endX,endY = digestLine(line)
        for i in range(startX, endX + 1):
            for k in range(startY, endY + 1):
                if command == "ON":
                    lightGrid[i][k] = 1
                elif command == "OFF":
                    lightGrid[i][k] = 0
                elif command == "TOGGLE":
                    lightGrid[i][k] ^= 1

    print(sum(map(sum, lightGrid)))

def day6b():
    gridSize = 1000
    lightGrid = [[ 0 for i in range(gridSize) ] for k in range(gridSize) ]
    with open(sys.argv[1], "r") as f:
        lines = f.readlines()

    for line in lines:
        command,startX,startY,endX,endY = digestLine(line)
        for i in range(startX, endX + 1):
            for k in range(startY, endY + 1):
                if command == "ON":
                    lightGrid[i][k] += 1
                elif command == "OFF":
                    if lightGrid[i][k] != 0:
                        lightGrid[i][k] -= 1
                elif command == "TOGGLE":
                    lightGrid[i][k] += 2

    print(sum(map(sum, lightGrid)))

day6a()
day6b()
