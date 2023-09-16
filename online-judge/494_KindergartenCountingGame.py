# Made by Jhoan Buitrago 07/10/2021 dd/mm/aaaa

# Problem https://onlinejudge.org/external/4/494.pdf

import re
from sys import stdin

def main():
    line = stdin.readline()
    while line != "" and line != "stopls\n":
        arr = re.findall(r"[a-zA-Z]+", line) #Finds all words, also equal to "\w+"
        #print(arr)
        print(len(arr)) 
        line = stdin.readline()

main()
