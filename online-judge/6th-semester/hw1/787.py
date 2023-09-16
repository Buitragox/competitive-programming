#Sub arreglo máximo por productos

from sys import stdin

# Finding the combination of the left side of mid and the right side
# of mid 
def bestCrossing(A, low, mid, hi):
	#print(f"\nlow {low}, mid {mid}, hi {hi}")
	bestLeft = A[mid - 1]
	worstLeft = A[mid - 1]
	multLeft = A[mid - 1]
	left = mid - 2
	while left >= low:
		multLeft *= A[left]
		bestLeft = max(bestLeft, multLeft)
		worstLeft = min(worstLeft, multLeft)
		left -= 1
	#print(f"wl {worstLeft}, bl{bestLeft}")
	
	bestRight = A[mid]
	worstRight = A[mid]
	multRight = A[mid]
	right = mid + 1
	while right < hi:
		multRight *= A[right]
		bestRight = max(bestRight, multRight)
		worstRight = min(worstRight, multRight)
		right += 1
	#print(f"wr {worstRight}, br {bestRight}")
	#print(f"max {max(bestLeft*bestRight, worstLeft*worstRight)}")
	return max(bestLeft*bestRight, worstLeft*worstRight)

#Divide and Conquer
def subArrayMult(A, low, hi):
	ans = None
	if low == hi:
		ans = 0
	elif low + 1 == hi:
		ans = A[low]
	else:
		mid = low + ((hi - low) >> 1)
		
		#Find the largest between left side and right side of mid
		ans = max(subArrayMult(A, low, mid), 
				subArrayMult(A, mid, hi))
		
		#Look if there is a largest section 
		#that crosses the mid value
		ans = max(ans, bestCrossing(A, low, mid, hi))
	return ans


def main():
	line = stdin.readline()
	while line != "":
		allnumbers = []
		numbers = list(map(int, line.split()))
		allnumbers.extend(numbers)
		while allnumbers[-1] != -999999:
			line = stdin.readline()
			numbers = list(map(int, line.split()))
			allnumbers.extend(numbers)

		res = subArrayMult(allnumbers, 0, len(allnumbers)-1)
		print(res)

		line = stdin.readline()


main()