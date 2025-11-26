import sys
import math

def divisorGenerator(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor

def day20a():
    with open(sys.argv[1]) as f:
        data = int(f.readlines()[0])
        presents = 0
        i = 9
        while (presents < data):
            i += 1
            presents = 0
            for d in divisorGenerator(i):
                presents += d * 10

        print (i)

def day20b():
    with open(sys.argv[1]) as f:
        data = int(f.readlines()[0])
        presents = 0
        i = 9
        while (presents < data):
            i += 1
            presents = 0
            for d in divisorGenerator(i):
                if i/d <= 50:
                    presents += d * 11

        print (i)

day20a()
day20b()
