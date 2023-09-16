# Made by Jhoan Buitrago 07/10/2021 dd/mm/aaaa

# Problem https://onlinejudge.org/external/100/10082.pdf

from sys import stdin

def main():
    qwert = r"`1234567890-=qwertyuiop[]\asdfghjkl;'zxcvbnm,./"
    string = stdin.readline()
    while string != "":
        for c in string:
            
            if c == " " or c.lower() in ['a', 'q', 'z', '`']:
                print(c, end="")
            elif c != "\n":
                index = qwert.find(c.lower())
                toPrint = qwert[index - 1]
                if c.isupper:
                    toPrint = toPrint.upper()
                print(toPrint, end="")

        string = stdin.readline()

        print()


main()