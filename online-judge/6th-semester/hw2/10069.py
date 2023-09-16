# Jhoan Manuel Buitrago Chavez
# 8953846

from sys import setrecursionlimit
from sys import stdin
setrecursionlimit(1000000)


def distinctSub(text:str, sub:str, n:int, m:int):
	ans = None
	if m == 0:
		ans = 1
	elif m > n:
		ans = 0
	elif text[n - 1] == sub[m - 1]:
		res1 = distinctSub(text, sub, n - 1, m - 1)
		res2 = distinctSub(text, sub, n - 1, m)
		ans = res1 + res2
	else:
		ans = distinctSub(text, sub, n - 1, m)

	return ans

def distinctSubMemo(text:str, sub:str, 
					n:int, m:int, memo:dict):
	ans = None
	key = (n,m)
	if key in memo:
		ans = memo[key]
	else:
		if m == 0:
			ans = 1
		elif m > n:
			ans = 0
		else:
			ans = distinctSubMemo(text, sub, n - 1, m, memo)
			if text[n - 1] == sub[m - 1]:
				ans += distinctSubMemo(text, sub, n - 1, m - 1, memo)
		memo[key] = ans
		
	return ans

def distinctSubTab(text:str, sub:str):
	N = len(text)
	M = len(sub)
	tab = [[0 for _ in range(M + 1)] for _ in range(N + 1)]

	for n in range(N + 1):
		tab[n][0] = 1
	
	n = 0
	m = 1
	while n < N + 1:
		if m == M + 1:
			n += 1
			m = 1
		else:
			if m > n:
				tab[n][m] = 0
			else:
				tab[n][m] = tab[n - 1][m]
				if text[n - 1] == sub[m - 1]:
					tab[n][m] += tab[n - 1][m - 1]
			m += 1
	return tab[N][M]

def main():
	cases = int(stdin.readline())
	for _ in range(cases):
		text = stdin.readline().rstrip()
		sub = stdin.readline().rstrip()
		memo = {}
		res = distinctSubMemo(text, sub, len(text), len(sub), memo)
		#res = distinctSubTab(text, sub)

		print(res)

main()
