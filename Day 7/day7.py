from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = Path(SCRIPT_DIR, "input.txt")

input = []
with open(INPUT_FILE, "r", encoding="UTF-8") as f:
    for line in f:
        input.append(line)


class Tree(dict):
    """A tree implementation using python's autovivification feature."""
    def __missing__(self, key):
        value = self[key] = type(self)()
        return value

    #cast a (nested) dict to a (nested) Tree class
    def __init__(self, data={}):
        for k, data in data.items():
            if isinstance(data, dict):
                self[k] = type(self)(data)
            else:
                self[k] = data
                
pc = Tree()



currentdir = ""
dirstack = []
for line in input:
    if line.startswith("$ ls"):
        pass
    elif line.startswith("$ cd .."):
        currentdir = dirstack.pop()        
    elif line.startswith("dir "):
        line = line[4:]
        pc[dir]
    elif line.startswith("$ cd"):
        currentdir = line[5:]
        dirstack.append(currentdir)
        pc.