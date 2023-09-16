# Jhoan Manuel Buitrago Chavez
# 8953846
# 30/04/2022
# dd/mm/yyyy

# https://onlinejudge.org/external/100/10063.pdf

from sys import stdin

ans = []
string = ""

def knuth(n: int):
    if n == len(string):
        print(''.join(ans)) #print with join is a lot faster
        #print(*ans, sep='')
    else:
        e = string[n]
        for i in range(len(ans)):
            ans.insert(i, e)
            knuth(n+1)
            ans.pop(i)
        ans.append(e)
        knuth(n+1)
        ans.pop()


def main():
    global string
    line = stdin.readline().rstrip()
    while line != "":
        string = line
        knuth(0)
        line = stdin.readline().rstrip()
        if line != "":
            print()


main()