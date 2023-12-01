"""
Jhoan Buitrago
01/12/2023 dd/mm/yyyy

https://adventofcode.com/2023/day/1

Same as part 1 but digits can be text or numbers
"""

from sys import stdin

words_numbers = {"one": 1, "two": 2, "three": 3, "four": 4, 
                 "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

def get_first(line: str) -> int:
    """
    Find all substrings (maximum size 5) from left to right and
    stop when the first digit is found (text or number)
    """
    num = -1
    left = 0
    right = 0

    while num == -1 and left < len(line):
        #print(left, right)
        size = right - left + 1
        if size > 5 or right >= len(line): #look for next substring
            left += 1
            right = left - 1 # -1 to compensate the right += 1
        elif line[left].isnumeric(): #found numeric digit
            num = int(line[left])
        elif size >= 3: 
            num = words_numbers.get(line[left:right+1], -1)
        
        right += 1

    return num


def get_last(line: str) -> int:
    """
    Find all substrings (maximum size 5) from right to left and
    stop when the first digit is found (text or number)
    """
    num = -1
    right = len(line) - 1
    left = len(line) - 1

    while num == -1 and right >= 0: #look for next substring
        size = right - left + 1
        if size > 5 or right >= len(line):
            right -= 1
            left = right + 1
        elif line[right].isnumeric(): #found numeric digit
            num = int(line[right])
        elif size >= 3: 
            num = words_numbers.get(line[left:right+1], -1)
        
        left -= 1

    return num


def main():
    total = 0
    line = stdin.readline()
    while line != "":
        line = line.strip()

        first = get_first(line)
        last = get_last(line)

        tmp = first*10 + last
        total += tmp
        
        line = stdin.readline()

    print(total)


if __name__ == "__main__":
    main()
