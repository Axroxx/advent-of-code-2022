import bst

elvesbst = bst.BST
 
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

for elve in elves:
    elvesbst.insert(elves[elve])
    
print(elvesbst.get_max())



