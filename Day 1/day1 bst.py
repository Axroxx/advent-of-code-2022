from pathlib import Path
import re
from bst import *

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = Path(SCRIPT_DIR, "input.txt")

elves = RBTree()

with open(INPUT_FILE, "r", encoding="UTF-8") as f:
    temp = []
    for line in f:
        if line != "\n":
            temp.append(int(line.strip()))
            continue
        elves.insert(sum(temp))
        temp = []
elves.insert(sum(temp))

print(elves)

