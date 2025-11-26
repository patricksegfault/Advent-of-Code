import sys

def find_nth_overlapping(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+1)
        n -= 1
    return start

def replaceNth(s, source, target, n):
    inds = [i for i in range(len(s) - len(source)+1) if s[i:i+len(source)]==source]
    if len(inds) < n:
        return  # or maybe raise an error
    s = list(s)  # can't assign to string slices. So, let's listify
    s[inds[n-1]:inds[n-1]+len(source)] = target  # do n-1 because we start from the first occurrence of the string, not the 0-th
    return ''.join(s)

def day19a():
    with open(sys.argv[1]) as f:
        data = f.readlines()
        rules = []
        molecule = ''
        for line in data:
            line = line.strip()
            if (len(line) > 0):
                if "=>" in line:
                    rules.append(line.split(" => "))
                else:
                    molecule = line
        
        uniqueMolecules = []

        for rule in rules:
            i = 1
            mIndex = find_nth_overlapping(molecule, rule[0], i)
            while (mIndex > -1):
                newMolecule = replaceNth(molecule, rule[0], rule[1], i)
                if newMolecule not in uniqueMolecules:
                    uniqueMolecules.append(newMolecule)
                i += 1
                mIndex = find_nth_overlapping(molecule, rule[0], i)
        
        print (len(uniqueMolecules))

def day19b():
    with open(sys.argv[1]) as f:
        data = f.readlines()

        print("")

day19a()
day19b()
