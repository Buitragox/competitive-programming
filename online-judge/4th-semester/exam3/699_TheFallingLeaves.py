from sys import stdin, stdout

MAX_LENGTH = 300

leaves = [0 for _ in range(MAX_LENGTH)]
cin = 0
line = []

def reset():
    for i in range(MAX_LENGTH):
        leaves[i] = 0

def solve(index):
    global cin
    value = line[cin]
    #print(cin)
    cin += 1
    if(value != -1):
        leaves[index] += value
        solve(index - 1)
        solve(index + 1) 

def main():
    global cin, line
    cases = 1
    mid = MAX_LENGTH // 2
    line = list(map(int, stdin.readline().split()))
    while(line[0] != -1):
        #print(line)
        cin = 1
        reset()
        leaves[mid] = line[0]
        solve(mid - 1)
        solve(mid + 1)

        i = 0
        value = leaves[0]
        while(value == 0):
            i += 1
            value = leaves[i]
        
        print(f"Case {cases}:")
        cases += 1

        while(value != 0):
            stdout.write(str(value))
            i += 1
            value = leaves[i]
            if(value != 0):
                stdout.write(" ")
        print("\n")
        line = list(map(int, stdin.readline().split()))

main() 