import time

start = time.time()

rucksacks = {}
n = 0
with open("input.txt") as f:
    for line in f:
        line = line.strip()
        half = int(len(line)/2)
        rucksacks[n] = [line[:half],line[half:]]
        n += 1
                

common = []

def rucksackcheck(a,b):
    for j in range(len(a)):
        for k in range(len(b)):
            if a[j] == b[k]:
                return a[j] 
            
for i in rucksacks:
    a = rucksacks[i][0]
    b = rucksacks[i][1]
    common.append(rucksackcheck(a,b))
        
   
def valueconverter(char):
    # a-z 97-122 -> 1-26
    # A-Z 65-90  -> 27-52
    
    val = ord(char)
    
    if val > 96:
        return val-96
    return val-38

values = 0
for char in common:
    values += valueconverter(char)
    
print(values)

end = time.time()
print(end - start)