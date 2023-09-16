from sys import stdin

nrules = 0

def find_passwords(n:int, wdict:list, p:str, ans:list):
    if n == len(p):
        for i in range(len(ans)):
            print(ans[i], end = "")
        print()
    else:
        if p[n] == "#":
            for i in range(len(wdict)):
                ans.append(wdict[i])
                find_passwords(n + 1, wdict, p, ans)
                ans.pop()
        elif p[n] == "0":
            for i in range(10):
                ans.append(i)
                find_passwords(n + 1, wdict, p, ans)
                ans.pop()
    

def main():
    global nrules
    line = stdin.readline()
    while line != "":
        print("--")
        nwords = int(line)
        wdict = [stdin.readline().rstrip() for _ in range(nwords)]

        nrules = int(stdin.readline())

        patterns = [stdin.readline().rstrip() for _ in range(nrules)]

        for i in range(nrules):
            find_passwords(0, wdict, patterns[i], [])

        line = stdin.readline()


main()