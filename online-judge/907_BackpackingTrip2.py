# Jhoan Manuel Buitrago Chavez
# 8953846
# Solution with BS since DP was too slow

from sys import stdin

MAXN = 603

total = [0 for _ in range(MAXN)]

#You can walk max_dist in a day, when exceeded you have to sleep
def checkValid(max_dist, N, max_sleeps):
    sleeps = 0
    last_camp = 0
    i = 1
    valid = True
    while i <= N+1 and valid:
        travelled = total[i] - total[last_camp]
        #print(f"t: {travelled}, s: {sleeps}")
        if travelled > max_dist: #If walking to next camp is too much, sleep at the last one
            last_camp = i - 1
            sleeps += 1
            if total[i] - total[last_camp] > max_dist:
                valid = False
        elif travelled == max_dist and i != N+1: #Sleep when walked exact amount, except when finished
            last_camp = i
            sleeps += 1
            i += 1

        else:
            i += 1

        
        if sleeps > max_sleeps:
            valid = False

    return valid


#Search the minimum distance that can be walked such that you sleep k times 
#Valid value is hi, unvalid low
def binary_search(N, max_sleeps):
    low = 0
    hi = total[N + 1]
    while low + 1 != hi:
        mid = low + ((hi - low) >> 1)
        valid = checkValid(mid, N, max_sleeps)
        #print(mid, valid)
        if valid:
            hi = mid
        else:
            low = mid

    return hi

def main():
    line = stdin.readline()
    while line != "":
        N, k = map(int, line.split())

        for i in range(1, N+2):
            total[i] = total[i-1] + int(stdin.readline())

        sleeps = N if k > N else k #max sleeps is N
        if sleeps == 0:
            print(total[N + 1])
        else:
            print(binary_search(N, sleeps))
        line = stdin.readline()

main()