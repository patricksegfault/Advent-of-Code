import sys
import re

with open(sys.argv[1], 'r') as inFile:
    for line in inFile:
        line = line.strip()
        line = re.sub('!.','',line)
        line = re.sub('\\<.*?\\>','',line)

        curGroup = 1
        total = 0

        for c in line:
            if c == '{':
                total += curGroup
                curGroup += 1
            elif c == '}':
                curGroup -= 1
        print(total)
        

            
