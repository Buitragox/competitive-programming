# Jhoan Manuel Buitrago Chavez
# 8953846

from sys import stdin

# Weight = Value
# Es estrictamente > 50%

def knapsack(n:int, m:float, products:list, mem:dict) -> float:
    ans = None
    if (n, m) in mem:
        ans = mem[(n, m)]
    else:
        if n == 0 or m < 0: #Termino cuando m es negativo, es decir, se supero el 50%
            ans = 0
        else:
            p = products[n - 1]
            notInclude = knapsack(n - 1, m, products, mem) #Opción de no incluir P

            if p <= m: #Si me falta porcentaje para llegar a 50% con P incluido
                include = knapsack(n - 1, m - p, products, mem) + p #Opción de sumar P
                if include > m and notInclude > m: #Si ambas son solución tomo el mínimo
                    ans = min(include, notInclude)
                elif include <= m: #Solo NO incluir P es solución
                    ans = notInclude
                else: #Solo incluir P es solución
                    ans = include

            elif notInclude > m: # Si ambos son solución
                ans = min(notInclude, p)
            else: # Si sumar P es solución
                ans = p

        mem[(n, m)] = ans
    return ans

# minPer = 0.0

# def knapsackTB(i:int, curr:int, products:list, obj:int):
#     global minPer

#     if curr > obj:
#         minPer = min(minPer, curr)
#     elif i < len(products): #Todavía tengo elementos y curr sigue siendo menor
#         knapsackTB(i + 1, curr + products[i], products, obj) #Incluir i
#         knapsackTB(i + 1, curr, products, obj)#No incluir i


def main():
    global minPer
    n, x = map(int, stdin.readline().split())
    while n != 0:
        #minPer = 10000
        x -= 1
        products = []
        stockholder = 0
        for i in range(n):
            whole, dec = map(int, stdin.readline().split('.'))
            tmp = whole * 100 + dec
            if i == x:
                stockholder = tmp
            else:
                products.append(tmp)

        mem = {}

        percentaje = knapsack(len(products), 5000-stockholder, products, mem) + stockholder

        ans = round(stockholder/percentaje * 100, 2)
        print("{:.2f}".format(ans)) 

        n, x = map(int, stdin.readline().split())
        

main()
