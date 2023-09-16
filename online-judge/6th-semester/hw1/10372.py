#BS de superman
from sys import stdin
from math import sin, cos, pi, sqrt
# sin y cos funcionan en radianes

eps1 = 1e-6
eps2 = 1e-7

def checkValid(heights:list, dists:list, 
				v:float, alpha:float):
	vx = v * cos(alpha)
	vy = v * sin(alpha)
	d = 0
	check = True
	i = 0
	while i < len(heights) and check:
		h = heights[i]
		t1 = d/vx
		y1 = (vy*t1) - (4.9*t1*t1)
		d += dists[i]
		t2 = d/vx 
		y2 = (vy*t2) - (4.9*t2*t2)
		if (y1 + eps2) < h or (y2 + eps2) < h:
			check = False
		i += 1

	return check
		

def binarySearch(heights:list, dists:list, distMax:float):
	low = 0.0
	hi = pi/2 #90 grados en radianes
	v = 0
	while (hi - low) > eps1:
		mid = low + ((hi - low) / 2)
		#mid = (hi + low) / 2
		v = sqrt((4.9 * distMax)/(cos(mid)*sin(mid)))
		#v = round(v, 3)
		if checkValid(heights, dists, v, mid):
			hi = mid #Apuntar más abajo
		else:
			low = mid #Apuntar más arriba
	
	return hi, v


def main():
	line = stdin.readline()
	while line != "":
		n = int(line)
		heights = []
		dists = []
		distMax = 0.0
		for _ in range(n):
			h, d = map(float, stdin.readline().split())
			heights.append(h)
			dists.append(d)
			distMax += d

		alphaR, v = binarySearch(heights, dists, distMax)
		alphaD = alphaR*180/pi
		#alphaD = round(alphaD, 2)
		#v = round(v, 2)
		print("{:.2f} {:.2f}".format(alphaD, v))
		
		line = stdin.readline()
		
main()
		
