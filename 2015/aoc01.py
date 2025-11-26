import sys

def day1a():
    with open(sys.argv[1]) as f:
        data = f.readlines()[0]
        up = 0
        down = 0
        for c in data:
            if (c == '('):
                up += 1
            elif (c == ')'):
                down += 1
        print(up - down)

def day1b():
    with open(sys.argv[1]) as f:
        data = f.readlines()[0]
        curF = 0
        pos = 0
        for c in data:
            if (c == '('):
                curF += 1
            elif (c == ')'):
                curF -= 1
            pos += 1
            if (curF < 0):
                break;
        print(pos)

day1a()
day1b()
