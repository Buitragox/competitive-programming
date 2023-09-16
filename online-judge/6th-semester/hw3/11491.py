from sys import stdin

## Solution casting whole number to int 
## inneficient because number big :(
# def solve(number, digits, erase):
#     number = int(number)
#     ans = 0
#     ans_len = 0
#     max_len = digits - erase
#     ans_mult = 10**(digits - erase - 1)
#     number_op = 10**(digits - 1)
#     last = 0
#     while erase > 0 and ans_len < max_len:
#         max_digit = 0
#         copy = number
#         c_op = number_op
#         pos = last
#         for i in range(erase + 1):
#             digit = copy // c_op
#             copy %= c_op
#             c_op //= 10
#             if digit > max_digit:
#                 max_digit = digit
#                 pos = last + i

#         ans += max_digit * ans_mult
#         ans_len += 1
#         erase -= (pos - last)
#         ans_mult //= 10
#         number_op //= 10**(pos - last)
#         number %= number_op
#         number_op //= 10
#         last += 1
    
#     if ans_len < max_len:
#         ans += number

#     return ans


def solve(number, digits, erase):
    ans = ""
    ans_len = 0
    max_len = digits - erase
    last = 0
    while erase > 0 and ans_len < max_len:
        max_digit = 0
        max_str = "0"
        pos = last
        for i in range(last, last + erase + 1):
            n = int(number[i])
            if n > max_digit:
                max_digit = n
                max_str = number[i]
                pos = i
        ans += max_str
        ans_len += 1
        erase -= (pos - last)
        last = pos + 1

    if ans_len < max_len:
        ans += number[last]
    return ans


def main():
    digits, erase = map(int, stdin.readline().split())
    while digits > 0:
        number = stdin.readline().rstrip()
        #print(number)
        ans = solve(number, digits, erase)
        print(ans)
        digits, erase = map(int, stdin.readline().split())
        

main()