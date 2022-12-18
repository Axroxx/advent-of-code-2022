"""
Advent of Code 2022, Day 06
"""
import timeit
from pathlib import Path
from tqdm import tqdm

start = timeit.timeit()

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = Path(SCRIPT_DIR, "input.txt")

def get_index_of_first_unique_str(buffer, size):
    """Get index of 1st unique string of length n in a buffer"""
    unique_str = []

    for index, char in enumerate(buffer):
        if len(unique_str) == size:
            return index

        if char in unique_str:
            last_found_index = unique_str.index(char)
            unique_str = unique_str[last_found_index+1:]

        unique_str.append(char)

    return unique_str


with open(INPUT_FILE, "r", encoding="UTF-8") as str_file:
    txt = str_file.read().splitlines()



for i in tqdm(range(10000),
              desc="Loading…",
              ascii=False, ncols=75):
    for buffer in txt:
        # part 2
        get_index_of_first_unique_str(buffer, 14)

stop = timeit.timeit()
print(stop-start)

print("Complete.")
