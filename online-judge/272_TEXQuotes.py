from sys import stdin, stdout

def main():
    line = stdin.readline()
    flag = True
    while line != "" and line != "stop":
        
        ans = ""
        for i in range(len(line)):
            if line[i] == '"':
                if flag:
                    ans += "``"
                else:
                    ans += "''"
                flag = not flag
            else:
                ans += line[i]
        stdout.write(ans)
        line = stdin.readline()


main()