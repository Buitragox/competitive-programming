# Jhoan Manuel Buitrago Chavez
# 8953846
# 29/04/2022
# dd/mm/yyyy

# https://onlinejudge.org/external/11/1193.pdf

from sys import stdin


def greedy_radars(P: list, D: float):
    """
    Sort by less X value, then by higher Y value.
    """
    P.sort(key = lambda x: (x[0], -x[1]))
    N = len(P)
    ans = 0
    i = 0
    while i < N and P[i][1] <= D:

        L = P[i]
        x = P[i][0]
        y = P[i][1]

        #Put the radar as far to the right as possible
        #such that the isle is in the border of the circuference
        if y < D:
            x += (D*D - y*y)**(1/2) 
        
        last_center = x

        ans += 1
        i += 1

        last_inside = True
        
        while i < N and P[i][1] <= D and last_inside:
            newcenter = P[i][0]
            y = P[i][1]
            if y < D:
                newcenter += (D*D - y*y)**(1/2)
            dist = ((L[0] - newcenter)**2 + L[1]**2)**(1/2)
            old_dist = ((P[i][0] - last_center)**2 + P[i][1]**2)**(1/2)

            if dist <= D: #If can upgrade last_center
                L = P[i] #Then most outside point is newpoint
                last_center = newcenter #upgrade last_center
                i += 1
            
            #Cant upgrade, check if isle is at least inside the circle
            elif old_dist <= D: 
                i += 1
            
            #If isle is not inside, nor can create a new circle
            #such that every previous isle is inside
            #then another radar is needed.
            else:
                last_inside = False

    if i != N: #If an isle.y > D, then answer is impossible.
        ans = -1    
        
    return ans


def main():
    N, D = map(int, stdin.readline().split())
    cases = 0
    while N != 0:
        cases += 1
        P = []
        for _ in range(N):
            x, y = map(int, stdin.readline().split())
            P.append((x, y))
        ans = greedy_radars(P, D)
        print(f"Case {cases}: {ans}")

        stdin.readline()
        N, D = map(int, stdin.readline().split())

main()
