from sys import stdin
from collections import deque

changeX = [-1, 0, 1, 0]
changeY = [0, 1, 0, -1]

def visitEmpty(x, y, visited, image):
    length = len(image[0])
    lines = len(image)
    bfsQueue = deque()
    bfsQueue.append((x, y))
    visited[x][y] = True
    while len(bfsQueue) != 0:
        pos = bfsQueue.popleft()
        for i in range(4):
            newX = pos[0] + changeX[i]
            newY = pos[1] + changeY[i]
            if newX >= 0 and newX < lines and newY >= 0 and newY < length:
                if image[newX][newY] == '0' and not visited[newX][newY]:
                    bfsQueue.append((newX, newY))
                    visited[newX][newY] = True
                    

def bfsAux(posX, posY, visited, image):
    length = len(image[0])
    lines = len(image)
    count = 0
    bfsQueue = deque()
    bfsQueue.append((posX, posY))
    visited[posX][posY] = True
    while len(bfsQueue) != 0:
        pos = bfsQueue.popleft()
        for i in range(4):
            newX = pos[0] + changeX[i]
            newY = pos[1] + changeY[i]
            if newX >= 0 and newX < lines and newY >= 0 and newY < length:
                if image[newX][newY] == '1' and not visited[newX][newY]:
                    bfsQueue.append((newX, newY))
                    visited[newX][newY] = True
                elif image[newX][newY] == '0' and not visited[newX][newY]:
                    count += 1
                    visitEmpty(newX, newY, visited, image)
    return count          

def bfs(visited, image):
    global count
    length = len(image[0])
    letters = ["W", "A", "K", "J", "S", "D"]
    res = ""
    for i in range(len(image)):
        for j in range(length):
            if image[i][j] == '1' and not visited[i][j]:
                count = bfsAux(i, j, visited, image)
                res += letters[count]
    return res


def main():
    lines, length = list(map(int, stdin.readline().split()))
    case = 1
    while(lines != 0 and length != 0):
        image = []
        length *= 4
        empty = "0" * (length + 2)
        image.append(empty)
        while lines:
            lines -= 1
            numBin = bin(int(stdin.readline(), 16))[2:]
            if len(numBin) != length:
                l = length - len(numBin)
                numBin = ("0" * l) + numBin
            numBin = "0" + numBin + "0"
            image.append(numBin)
        image.append(empty)
        visited = [[False for _ in range(length + 2)] for _ in range(len(image))]
        visitEmpty(0, 0, visited, image)
        res = "".join(sorted(bfs(visited, image)))
        print(f"Case {case}: {res}")
        case += 1
        lines, length = list(map(int, stdin.readline().split()))

main()