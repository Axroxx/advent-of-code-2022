elves = {}
templist = []
with open("input.txt") as f:
    i = 0
    for line in f:
        if line != "\n":
           templist.append(int(line.strip()))
        else:
            elves[i] = templist
            templist = []
            i += 1
elves[i] = templist

temp = 0
max = 0
small = 0
top3 = [0,0,0]
print(min(top3))
for j in elves:
    for item in elves[j]:
        temp += item
    small = min(top3)
    print(top3)
    if temp > small:
        for k in range(len(top3)):
            if top3[k] == small:
                top3[k] = temp
                break
    temp = 0

sum = 0
for item in top3:
    sum += item
print(sum)

