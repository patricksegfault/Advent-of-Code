import sys
import hashlib

def day04a():
    with open(sys.argv[1], 'r') as f:
        sKey = f.readlines()[0]
        i = 1
        md5 = hashlib.md5((sKey + str(i)).encode("utf-8")).hexdigest()
        
        while(md5[0:5] != "00000"):
            i += 1
            md5 = hashlib.md5((sKey + str(i)).encode("utf-8")).hexdigest()

        print(i)

def day04b():
    with open(sys.argv[1], 'r') as f:
        sKey = f.readlines()[0]
        i = 1
        md5 = hashlib.md5((sKey + str(i)).encode("utf-8")).hexdigest()
        
        while(md5[0:6] != "000000"):
            i += 1
            md5 = hashlib.md5((sKey + str(i)).encode("utf-8")).hexdigest()

        print(i)

day04a()
day04b()
