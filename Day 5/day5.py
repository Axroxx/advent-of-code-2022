from pathlib import Path
import re

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = Path(SCRIPT_DIR, "input.txt")
stacks = {}
rows = []
instructions = {}
n = 0

with open(INPUT_FILE, "r", encoding="UTF-8") as f:
    for line in f:
        line = line
        if not line.startswith(" 1") and not line.startswith("move"):
            
            row = 0
            for i in range(1,len(line),4):
                
                if line[i] != " ":
                    rows.append([row,line[i]])
                row += 1
                    
        else:
            if line.startswith("move"):
                tempinstruction = []
                line = line.strip()
                tempinstruction = re.split("move | from | to ", line)
                
                tempinstruction.remove("")
                for i in range(len(tempinstruction)): 
                    tempinstruction[i] = int(tempinstruction[i])
                    
                instructions[n] = tempinstruction
                n += 1
                


for row in reversed(rows):
    try:
        stacks[row[0]]
    except:
        stacks[row[0]] = []
    stacks[row[0]].append(row[1])


for instruction in instructions:
    tempstack = stacks[instruction[2]-1]
    for i in range(instruction[0]):
        tempstack.append()