# Jhoan Manuel Buitrago Chavez
# 8953846
# 14/04/2022
# dd/mm/yyyy

# Problem link: https://onlinejudge.org/external/111/11127.pdf

# Python is too slow for this problem

#Code version without break instruction

from sys import stdin

counter = 0
changes = ['0', '1']
N = 0
pattern = 0
last_asterisk = 0


#Check if there is a triple SSS in the string pattern[:(i+1)]
def has_triple(i: int):
    triple = False #If True, a triple (SSS) was found
    M = i + 1
    disp = 1 #displacement
    
    while disp <= (M // 3) and not triple:
        k = 0
        equal = True
        while k < disp and equal:
            if pattern[i - k] != pattern[i - k - disp] or \
               pattern[i - k] != pattern[i - k - (disp * 2)]:
               equal = False
            k += 1
        
        if equal:
            triple = True
        
        disp += 1
    
    return triple


def count_triple_free(i: int):
    global counter
    if i == N:
        counter += 1

    elif i == last_asterisk:
        is_triple = False
        k = i
        while k < N and not is_triple:
            if not(i < 2 or not has_triple(k)):
                is_triple = True
            k += 1
        
        if not is_triple:
            counter += 1

    elif pattern[i] == '*':
        for p in changes:
            pattern[i] = p
            if i < 2 or not has_triple(i):
                count_triple_free(i + 1)
        pattern[i] = '*'

    elif i < 2 or not has_triple(i):
        count_triple_free(i + 1)


def main():
    global counter, N, pattern, last_asterisk
    line = stdin.readline().rstrip()
    cases = 0
    while line != "0":
        cases += 1
        counter = 0
        strN, strPattern = list(line.split())
        N = int(strN)
        pattern = list(strPattern)

        last_asterisk = N
        while last_asterisk >= 0 and pattern[last_asterisk - 1] != '*':
            last_asterisk -= 1
            
        count_triple_free(0)

        print(f"Case {cases}: {counter}")

        line = stdin.readline().rstrip()


main()