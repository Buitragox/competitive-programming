"""
Jhoan Buitrago
01/12/2023 dd/mm/yyyy

https://adventofcode.com/2023/day/1

For each line of text, look for the first and last digits and combine them 
(ej: a71six14rk = 74)

Sum all results
"""

from sys import stdin


def get_first(line: str) -> int:
    first = 0
    for i in range(len(line)):
        if line[i].isnumeric():
            first = int(line[i])
            break

    return first


def get_last(line: str) -> int:
    last = 0
    for i in range(len(line)-1, -1, -1):
        if line[i].isnumeric():
            last = int(line[i])
            break
    
    return last


def main():
    total = 0
    line = stdin.readline()
    while line != "":
        first = get_first(line)
        last = get_last(line)
        
        total += first*10 + last 
        line = stdin.readline()
        
    print(total)
        

if __name__ == "__main__":
    main()
