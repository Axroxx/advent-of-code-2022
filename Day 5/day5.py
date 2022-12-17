from pathlib import Path
import re

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = Path(SCRIPT_DIR, "input.txt")
stacks = {}
rows = []
instructions = []
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
                    tempinstruction[i] = int(tempinstruction[i])-1
                    
                instructions.append(tempinstruction)
                n += 1
                


for row in reversed(rows):
    try:
        stacks[row[0]]
    except:
        stacks[row[0]] = []
    stacks[row[0]].append(row[1])

stackList = []
for stack in stacks:
    stackList.append(stacks[stack])

stackList.reverse()

part1 = False

#part 1

if part1:
    for instruction in instructions:
        for i in range(instruction[0]+1):
            stackList[instruction[2]].append(stackList[instruction[1]].pop())
  
    
#part 2

if not part1:
    for instruction in instructions:
        tempstack = []
        for i in range(instruction[0]+1):
            tempstack.append(stackList[instruction[1]].pop())
        
        for item in reversed(tempstack):
            stackList[instruction[2]].append(item)
            
            
#end

for stack in stackList:
    print(stack.pop(),end="")