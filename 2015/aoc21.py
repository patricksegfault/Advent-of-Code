import sys
import itertools

def canWin(heroHp, heroDmg, heroAmr, bossHp, bossDmg, bossAmr):
    while (bossHp >= 0 and heroHp >= 0):
        bossHp -= 1 if heroDmg - bossAmr < 1 else heroDmg - bossAmr
        heroHp -= 1 if bossDmg - heroAmr < 1 else bossDmg - heroAmr

    return True if bossHp <= 0 else False

def calcCost(w, a, r):
    return w[0] + a[0] + r[0][0] + r[1][0]

def day21a(weapons, armor, rings):
    with open(sys.argv[1]) as f:
        data = f.readlines()
        bossHp = int(data[0].split(": ")[1])
        bossDmg = int(data[1].split(": ")[1])
        bossAmr = int(data[2].split(": ")[1])
        minCost = 10000
        
        for w in weapons:
            for a in armor:
                for r in itertools.combinations(rings, 2):
                    if (canWin(100, w[1] + r[0][1] + r[1][1], a[1] + r[0][2] + r[1][2], bossHp, bossDmg, bossAmr)):
                        cost = calcCost(w, a, r)
                        minCost = cost if cost < minCost else minCost

        print (minCost)

def day21b(weapons, armor, rings):
    with open(sys.argv[1]) as f:
        data = f.readlines()
        bossHp = int(data[0].split(": ")[1])
        bossDmg = int(data[1].split(": ")[1])
        bossAmr = int(data[2].split(": ")[1])
        maxCost = 0
        
        for w in weapons:
            for a in armor:
                for r in itertools.combinations(rings, 2):
                    if (not canWin(100, w[1] + r[0][1] + r[1][1], a[1] + r[0][2] + r[1][2], bossHp, bossDmg, bossAmr)):
                        cost = calcCost(w, a, r)
                        maxCost = cost if cost > maxCost else maxCost

        print (maxCost)

weapons = [[8, 4], [10, 5], [25, 6], [40, 7], [74, 8]]
armor = [[0, 0], [13, 1], [31, 2], [53, 3], [75, 4], [102, 5]]
rings = [[0, 0, 0], [0, 0, 0], [25, 1, 0], [50, 2, 0], [100, 3, 0], [20, 0, 1], [40, 0, 2], [80, 0, 3]]

day21a(weapons, armor, rings)
day21b(weapons, armor, rings)


