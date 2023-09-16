#Votaciones

from sys import stdin
from math import ceil

def checkValid(cities:list, boxSize:int, nboxes:int):
	for c in cities:
		b = ceil(c / boxSize)
		nboxes -= b
		if nboxes < 0:
			return False

	return True


def binarySearch(cities:list, nboxes:int):
	hi = max(cities)
	low = 0
	while low + 1 != hi:
		mid = low + ((hi - low) >> 1)
		if checkValid(cities, mid, nboxes):
			hi = mid
		else:
			low = mid

	return hi
	

def main():
	n, nboxes = map(int, stdin.readline().split())
	while n != -1 and nboxes != -1:
		cities = []
		for _ in range(n):
			cities.append(int(stdin.readline()))
	
		answer = binarySearch(cities, nboxes)
		print(answer)
		input()
		n, nboxes = map(int, stdin.readline().split())

main()