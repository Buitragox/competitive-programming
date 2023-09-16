from sys import stdin

def binarySearch(indices:dict, last:int):
	hi = len(indices) - 1
	low = -1
	while low + 1 != hi:
		mid = low + ((hi - low) >> 1)
		if indices[mid] > last:
			hi = mid
		else:
			low = mid
	return indices[hi]


def solve(letterIndex:dict, query:str):
	first = -1
	last = -1
	i = 0
	check = True
	while i < len(query) and check:
		if query[i] in letterIndex:
			index = binarySearch(letterIndex[query[i]], last)
			if first == -1:
				first = index
			if index > last:
				last = index
			else:
				check = False
		else:
			check = False
		i += 1

	if not check:
		last = -1

	return first, last


def main():
	S = stdin.readline().rstrip('\n')
	Q = int(stdin.readline())
	letterIndex = {}
	for i in range(len(S)):
		letter = S[i]

		if letter in letterIndex:
			letterIndex[letter].append(i)
		else:
			letterIndex[letter] = [i]

	for _ in range(Q):
		query = stdin.readline().rstrip('\n')
		first, last = solve(letterIndex, query)
		if last == -1:
			print("Not matched")
		else:
			print("Matched", first, last)

main()