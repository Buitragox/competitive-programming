from sys import stdin

# Weight = Value

def knapsack(n:int, m:float, products:list, mem:dict):
    ans = None
    if (n, m) in mem:
        ans = mem[(n, m)]
    else:
        if n == 0 or m < 0:
            ans = 0
        else:
            p = products[n - 1]
            notInclude = knapsack(n - 1, m, products, mem) 
            if p <= m:
                include = knapsack(n - 1, m - p, products, mem) + p

                if include > m and notInclude > m:
                    ans = min(include, notInclude)
                elif include <= m:
                    ans = notInclude
                else:
                    ans = include

            elif notInclude > m:
                ans = min(notInclude, p)

            else:
                ans = p
        mem[(n, m)] = ans
    print(n, m, ans)
    return ans

minPer = 0.0

def knapsackTB(i:int, curr:int, products:list, obj:int):
    global minPer

    if curr > obj:
        minPer = min(minPer, curr)
    elif i < len(products): #Todavía tengo elementos y curr sigue siendo menor
        knapsackTB(i + 1, curr + products[i], products, obj) #Incluir i
        knapsackTB(i + 1, curr, products, obj)#No incluir i


def main():
    global minPer
    #count = 0
    n, x = map(int, stdin.readline().split())
    while n != 0:
        minPer = 10000
        x -= 1
        products = []
        stockholder = 0
        for i in range(n):
            whole, dec = map(int, stdin.readline().split('.'))
            tmp = whole * 100 + dec
            #print(tmp)
            if i == x:
                stockholder = tmp
            else:
                products.append(tmp)

        #print(products, stockholder)
        mem = {}
        #print(products)

        percentaje = knapsack(len(products), 5000-stockholder, products, mem) + stockholder
        print(percentaje - stockholder)
        print(stockholder)
        print(percentaje)
        #knapsackTB(0, stockholder, products, 5000) #/ 100
        #percentaje = minPer
        #print(stockholder/percentaje * 100)
        ans = round(stockholder/percentaje * 100, 2)
        print("{:.2f}".format(ans)) 

        # count += 1
        # if count == 13:
        #     print(n, x, products, stockholder)
        #     break

        n, x = map(int, stdin.readline().split())
        


main()
