#12/09/2019 dd/mm/yyyy

finalOutput = ""

cases = int(input())

for case in range(cases):
    arr = []
    pointer = 0
    for i in range(100):
        arr.append(0)

    commands = input()

    for j in range(len(commands)):
        if commands[j] == ">":
            pointer += 1
            if pointer > 99:
                pointer = 0
        elif commands[j] == "<":
            pointer -= 1
            if pointer < 0:
                pointer = 99
        elif commands[j] == "+":
            arr[pointer] += 1
            if arr[pointer] > 255:
                arr[pointer] = 0
        elif commands[j] == "-":
            arr[pointer] -= 1
            if arr[pointer] < 0:
                arr[pointer] = 255

    output = "Case " + str(case + 1) + ": "
    for k in range(100):
        num = hex(arr[k])[2:]
        num2 = num.upper()
        if len(num2) == 1:
            num2 = "0" + num2
        output += str(num2) + " "
    
    output = output[:-1]

    finalOutput += output
    finalOutput += "\n"

print(finalOutput[:-1])
