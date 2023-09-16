#Jhoan Manuel Buitrago Chavez
#8953846

from sys import stdin

ans = [''] * int(1e5)

def solve(number, digits, erase):
    global ans
    ans_len = 0
    max_len = digits - erase
    last = 0
    min_ord = ord('0')
    while erase > 0 and ans_len < max_len:
        max_str = '0'
        max_digit = min_ord
        pos = last
        for i in range(last, last + erase + 1):
            n = ord(number[i])
            if n > max_digit:
                max_digit = n
                max_str = number[i]
                pos = i
        ans[ans_len] = max_str
        ans_len += 1
        erase -= (pos - last)
        last = pos + 1

    if ans_len < max_len:
        #ans.extend(c for c in number[last:])
        for i in range(last, digits):
            ans[ans_len] = number[i]
            ans_len += 1


def main():
    digits, erase = map(int, stdin.readline().split())
    while digits > 0:
        number = stdin.readline().rstrip()
        #print(number)
        solve(number, digits, erase)
        max_len = digits - erase
        for i in range(max_len):
            print(ans[i], end="")
        print()
        digits, erase = map(int, stdin.readline().split())
        

main()