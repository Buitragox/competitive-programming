from sys import stdin

def main():
    line = stdin.readline()
    while line != "":
        stack = []
        matriList = list(map(int, line.split()))
        size = len(matriList)
        for i in range(0, size):
            if matriList[i] < 0 and len(stack) == 0:
                stack.append([matriList[i], 0])
            elif matriList[i] < 0:
                stack[-1][1] += matriList[i]
                if stack[-1][1] <= stack[-1][0]:
                    break;
                stack.append([matriList[i], 0])
            elif matriList[i] > 0 and len(stack) > 0:
                if matriList[i] * (-1) == stack[-1][0]:
                    stack.pop()
                else:
                    stack.append([matriList[i], 0])
                    break;
            else:
                stack.append([matriList[i], 0])
                break;

        if len(stack) == 0:
            print(":-) Matrioshka!")
        else:
            print(":-( Try again.")

        line = stdin.readline()


main()