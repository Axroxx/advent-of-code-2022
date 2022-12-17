match = {}
nr = 0

with open("input.txt") as f:
    for line in f:
        match[nr] = line.strip()
        nr += 1

opp = 0
extra = 0
score = 0

for i in match:
    oppt = match[i][0]
    plrt = match[i][2]

    if oppt == "A":     #Rock  
        opp = 1
    elif oppt == "B":   #Paper
        opp = 2
    else:               #Scissors
        opp = 3
    
    
    if plrt == "Y":
        score += 3 + opp

    elif plrt == "Z":
        score += 6 + ( opp % 3 ) + 1

    else:
        score += (( opp + 1 ) % 3 ) + 1


print(score)

#10274