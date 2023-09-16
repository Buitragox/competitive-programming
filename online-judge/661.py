#12/09/2019 dd/mm/yyyy

finalOutput = ""

nmc = input()
nmcList = nmc.split()
count = 1
while nmcList != ["0", "0", "0"]:
    numberDevices = int(nmcList[0])
    numberOperations = int(nmcList[1])
    fuseCapacity = int(nmcList[2])
    ampDevices = []
    stateDevices = []
    currentAmp = 0
    maxAmp = 0
    blown = False
    for i in range(numberDevices):
        device = int(input())
        ampDevices.append(device)
        stateDevices.append(0)

    for j in range(numberOperations):
        op = int(input()) - 1
        if stateDevices[op] == 0:
            stateDevices[op] = 1
            currentAmp += ampDevices[op]
            if currentAmp > fuseCapacity:
                blown = True
            elif currentAmp > maxAmp:
                maxAmp = currentAmp
        elif stateDevices[op] == 1:
            stateDevices[op] = 0
            currentAmp -= ampDevices[op]

    output = "Sequence " + str(count) + "\n"
    if blown:
        output += "Fuse was blown.\n\n"
    else:
        output += "Fuse was not blown.\n"
        output += "Maximal power consumption was " + str(maxAmp) + " amperes.\n\n"
    
    finalOutput += output

    nmc = input()
    nmcList = nmc.split()
    count += 1

print(finalOutput[:-1])
