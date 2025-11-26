import sys
import re

def day5a():
    with open(sys.argv[1]) as f:
        data = f.readlines()
        nice = 0
        doub = re.compile(r".*([a-z])\1.*")
        vowel = re.compile(r".*([aeiou]).*([aeiou]).*([aeiou]).*")
        bad = re.compile(r".*(ab|cd|pq|xy).*")

        for w in data:
            if (doub.match(w) and vowel.match(w) and bad.match(w) == None):
                nice += 1

        print (nice)

def day5b():
    with open(sys.argv[1]) as f:
        data = f.readlines()
        nice = 0
        doubPair = re.compile(r".*([a-z][a-z]).*\1.*")
        skipPair = re.compile(r".*([a-z]).\1.*")

        for w in data:
            if (doubPair.match(w) and skipPair.match(w)):
                nice += 1

        print (nice)

day5a()
day5b()
