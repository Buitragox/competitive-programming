#12/10/2019 dd/mm/yyyy

amount = int(input())
finalOutput = ""

while amount != 0:
    first = True
    listNumbers = []
    numbers = input().split()
    for i in range(amount):
        numbers[i] = int(numbers[i])
    
    suma = 0
    cost = 0
    while len(numbers) > 1:
        numbers = sorted(numbers)
        suma = numbers.pop(0)
        numbers[0] += suma
        cost += numbers[0]

    finalOutput += str(cost) + "\n"
    amount = int(input())

print(finalOutput[:-1])

        
                
