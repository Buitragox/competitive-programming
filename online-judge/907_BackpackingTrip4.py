# Jhoan Manuel Buitrago Chavez
# 8953846
# Fastest solution idk why but ok

from sys import stdin

MAXN = 603

dist = [0 for _ in range(MAXN)]

#You can walk max_dist in a day, when exceeded you have to sleep
def checkValid(max_dist, N, max_sleeps):
    sleeps = 0
    i = 1
    valid = True
    travelled = 0
    #while loop slows it down a lot apparently
    while i <= N+1 and valid:
        travelled += dist[i]
        if travelled > max_dist: #If walking to next camp is too much, sleep at the last one
            travelled = dist[i]
            sleeps += 1

        if sleeps > max_sleeps:
            valid = False
        i += 1

    return valid


#Search the minimum distance that can be walked such that you sleep k times 
#Valid value is hi, unvalid low
def binary_search(N, max_sleeps, max_single, total):
    low = 0
    hi = total
    while low + 1 != hi:
        mid = low + ((hi - low) >> 1)
        if mid >= max_single and checkValid(mid, N, max_sleeps):
            hi = mid
        else:
            low = mid
    return hi


def main():
    line = stdin.readline()
    while line != "":
        N, k = map(int, line.split())
        max_single = 0
        total = 0
        for i in range(1, N+2):
            tmp = int(stdin.readline())
            dist[i] = tmp
            total += tmp
            max_single = max(max_single, tmp)

        sleeps = N if k > N else k #max sleeps is N
        if sleeps == 0: #Optimization?
            print(total)
        elif sleeps == N: #Optimization?
            print(max_single)
        else:
            print(binary_search(N, sleeps, max_single, total))
        line = stdin.readline()

main()