assignments = {}
n = 0
with open("input.txt") as f:
    for line in f:
        line = line.strip()
        i = 0
        while line[i] != ",":
            i += 1
        assignments[n] = [line[:i],line[i+1:]]
        temp = []
        for assignment in assignments[n]:  
            i = 0
            while assignment[i] != "-":
                i += 1
            temp.append(int(assignment[:i]))
            temp.append(int(assignment[i+1:]))
        
        assignments[n] = [[temp[0],temp[1]],[temp[2],temp[3]]]
        n += 1  
        
overlap = 0
for k in assignments:
    print(assignments[k])
    thing = assignments[k]
    if (thing[0][1] <= thing[1][1] and thing[0][1] >= thing[1][0]) or (thing[0][0] >= thing[1][0] and thing[0][0] <= thing[1][1]) or (thing[0][0] <= thing[1][0] and thing[1][1] <= thing[0][1]):
        overlap += 1
        print("overlap")

print(overlap)

# 54 minutes