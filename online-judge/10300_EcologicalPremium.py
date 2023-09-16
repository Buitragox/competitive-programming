# Made by Jhoan Buitrago 03/10/2021 dd/mm/aaaa

# Problem https://onlinejudge.org/external/103/10300.pdf

cases = int(input())
for _ in range(cases):
    farmers = int(input())

    sumMoney = 0

    for _ in range(farmers):
        s, a, f = map(int, input().split())
        money = s * f #Formula is space/animals * friend * animals , you can cancel animals
        sumMoney += (money if a > 0 else 0) #You still cannot divide by 0

    print(sumMoney)