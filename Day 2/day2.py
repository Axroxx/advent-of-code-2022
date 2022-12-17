match = {}
nr = 0

with open("input.txt") as f:
    for line in f:
        match[nr] = line.strip()
        nr += 1

opp = 0
plr = 0
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

    if plrt == "X":     #Rock
        plr = 1
    elif plrt == "Y":   #Paper
        plr = 2
    else:               #Scissors
        plr = 3
    
    if opp == plr:
        score += 3 + plr 
    elif plr-opp % 3 == 1:
        score += 6 + plr
    else:
        score += plr

print(score)
