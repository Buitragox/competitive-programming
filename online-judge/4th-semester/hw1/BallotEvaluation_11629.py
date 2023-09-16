from sys import stdin

def main():
    numbers = stdin.readline()
    nSplit = numbers.split()
    amountP = int(nSplit[0])
    amountG = int(nSplit[1])
    parties = {}
    for i in range(0, amountP):
        line = stdin.readline()
        parts = line.split()
        floatNumber = parts[1].split(".")
        parties[parts[0]] = int(floatNumber[0]) * 10 + int(floatNumber[1])
    
    for j in range(0, amountG):
        line = stdin.readline()
        parts = line.split()
        numbGuess = int(parts[-1]) * 10
        operation = parts[-2]
        size = len(parts) - 2
        numbReal = 0
        guess = True
        
        for k in range(0, size + 1, 2):
            numbReal += parties[parts[k]]
        if operation == ">":
            guess = numbReal > numbGuess
        elif operation == ">=":
            guess = numbReal >= numbGuess
        elif operation == "<":
            guess = numbReal < numbGuess
        elif operation == "<=":
            guess = numbReal <= numbGuess
        else:
            guess = numbReal == numbGuess
        
        if guess:
            print("Guess #" + str(j + 1) + " was correct.")
        else:
            print("Guess #" + str(j + 1) + " was incorrect.")

main()