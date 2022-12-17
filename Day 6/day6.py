from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = Path(SCRIPT_DIR, "input.txt")

string = ""

with open(INPUT_FILE, "r", encoding="UTF-8") as f:
    string = f.read()

unique = []
amt = 0

for i in range(len(string)):
    if len(unique) == 14:   #4/14 for part 1/2
        amt = i
        break
    if string[i] not in unique:
        unique.append(string[i])
    else:
        unique = []      
    
print(unique)
print(amt)