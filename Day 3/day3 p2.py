import time

start = time.time()

rucksacks = {}
n = 0
with open("input.txt") as f:
    for line in f:
        rucksacks[n] = line.strip()
        n += 1  


def rucksackcheck(a,b,c):
    checked = []
    for i in range(len(a)):
        print(checked)
        char = a[i]
        if char not in checked:
            for j in range(len(b)):
                print(b[j])
                if char == b[j]:
                    for k in range(len(c)):
                        if char == c[k]:
                            return char
            checked.append(char)
                
                
common = []

j = 0     
#for i in range(0,len(rucksacks.keys()),3):
for i in range(0,1,3):
    a = rucksacks[i]
    b = rucksacks[i+1]
    c = rucksacks[i+2]
    print(a,b,c)
    common.append(rucksackcheck(a,b,c))
    
    print(common[j])
    j+=1
        
   
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