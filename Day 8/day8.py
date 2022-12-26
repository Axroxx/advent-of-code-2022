from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = Path(SCRIPT_DIR, "input.txt")

input = []
with open(INPUT_FILE, "r", encoding="UTF-8") as f:
    for line in f:
        input.append(str(line).strip())
    
    
xmax = {}
ymax = {}
mxmax = {}
mymax = {}

visible = 0
for y, line in enumerate(input):
    for x in range(len(line)):
        if line[x] < xmax[x][0]:
            
        try: 
            if line[x] > xmax[x][0]:
                xmax[x] = [line[x],y]
        except:
            xmax[x] = [line[x],y]
        

print(xmax)
