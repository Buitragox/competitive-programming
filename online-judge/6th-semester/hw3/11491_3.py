# Jhoan Manuel Buitrago Chavez
# 8953846
# 15/03/2022
# dd/mm/yyyy

# Best solution using deque, other solution kept iterating
# over already checked numbers.

from sys import stdin
from collections import deque

def erase_win(number:str, digits:int, erase:int):
    """
    -   Keep the highest possible digits in the deque
    -   Erase the rightmost digits if you find a higher digit
        (only if you have remaining erases)
    """
    ans = deque()
    max_len = digits - erase
    ans_len = 0 #Current ans length
    i = 0
    #Iterate over number
    while i < digits and erase > 0:
        d = number[i]
        n = ord(d) #ord is faster than casting to int
                   #and serves same purpose.

        #if last number is lower than current digit, try to delete
        while ans_len > 0 and ans[-1][1] < n and erase > 0: 
            ans.pop()
            erase -= 1
            ans_len -= 1
        ans.append((d, n))
        ans_len += 1
        i += 1

    #Delete excess digits
    while erase > 0:
        ans.pop()
        erase -= 1
        ans_len -= 1
        
    #Print stored numbers
    for d in ans:
        print(d[0], end = "")

    #Print the remaining solution instead of appending to ans
    if ans_len < max_len:
        print(number[i:], end = "")
    
    print() #\n

def main():
    digits, erase = map(int, stdin.readline().split())
    while digits > 0:
        number = stdin.readline().rstrip()
        
        erase_win(number, digits, erase)
        
        digits, erase = map(int, stdin.readline().split())
        

main()