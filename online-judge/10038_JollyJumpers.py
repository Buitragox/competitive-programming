from sys import stdin

def main():
    #Read until EOF
    line = stdin.readline()
    while line != "":
        #First element is size
        n, *parts = list(map(int, line.split()))#[1:]
        if n == 1:
            print("Jolly")
        else:
            jollySet = set()
            flag = True
            for i in range(n - 1):
                res = abs(parts[i] - parts[i + 1])
                if res > 0 and res < n:
                    jollySet.add(res)
                else:
                    flag = False
                    break

            if flag and len(jollySet) == n - 1:
                print("Jolly")
            else:
                print("Not jolly")
        line = stdin.readline()

main()