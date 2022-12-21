import timeit
from pathlib import Path
#from tqdm import tqdm

start = timeit.timeit()

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = Path(SCRIPT_DIR, "input.txt")

string = ""

with open(INPUT_FILE, "r", encoding="UTF-8") as f:
    string = f.read()

def py():

    unique = []
    amt = 0

    for i in range(len(string)):
        if len(unique) == 14:   #4/14 for part 1/2
            amt = i
            return 0
        if string[i] not in unique:
            unique.append(string[i])
        else:
            unique = []      



#for i in tqdm (range (10000), desc="Loading…", ascii=False, ncols=75):
    py()

stop = timeit.timeit()
print(stop-start)
