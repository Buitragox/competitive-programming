# Jhoan Manuel Buitrago Chavez
# 8953846
# 12/03/2022
# dd/mm/yyyy

from sys import stdin
from heapq import heappush, heappop, heappushpop

def choose_orders(order_list):
    order_list.sort() #Better to sort than use heap
    ans = 0
    accepted = []
    
    acum_time = 0
    for i in range(len(order_list)):
        due_date, time = order_list[i]
        if acum_time + time <= due_date: #If can add it, do it
            acum_time += time
            heappush(accepted, -time)
            ans += 1
        elif len(accepted) > 0: #Try to upgrade the acummulated finish time
            t = -accepted[0]
            #Remove 't', add 'time'
            if acum_time + time - t < acum_time: 
                acum_time += (time - t)
                heappushpop(accepted, -time) #not that much better
                # heappop(accepted)
                # heappush(accepted, -time)
    return ans
    

def main():
    cases = int(stdin.readline())
    while cases:
        stdin.readline() #blank line
        orders = int(stdin.readline())
        order_list = []
        for _ in range(orders):
            time, due_date = map(int, stdin.readline().split())
            order_list.append((due_date, time))
    
        ans = choose_orders(order_list)
        print(ans)
        if cases > 1:
            print()
        cases -= 1
    
main()