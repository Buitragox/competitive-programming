"""
dd/mm/yyyy
29/03/2022

Author: Jhoan Manuel Buitrago Chávez
Student Code: 8953846

Code of Honor:
As a member of the academic community of the Pontificia Universidad Javeriana Cali, 
I commit to follow the highest standards of academic integrity.

Problem 10076: The Bumpy Robot
https://onlinejudge.org/external/100/10076.pdf
"""

from sys import stdin
from math import ceil
from heapq import heappush, heappop

#Max size for the board
MAX_SIZE = 50

#Values needed for time and energy calculations
a1 = a2 = g = 0
b1 = b2 = d = 0

#order of movements: up, right, down, left
changeRow = [-1, 0, 1, 0]
changeCol = [0, 1, 0, -1]


class State:
    """
    Class that represents the states of the implicit graph
    
    Attributes
    ----------
    time : int
        Time required to get to board[row][col] on this state

    energy : int
        Energy wasted to get to board[row][col] on this state

    row : int
        The row value of the current position in the board

    col : int
        The column value of the current position in the board
    
    Methods
    ----------
    __lt__ : bool
        Define the 'less than' operator between states.
    
    __str__ : str
        Define the method to cast a State object to string. 
        Only used for debbuging and printing purposes.
            
    """
    
    def __init__(self, time:int, energy:int, row:int, col:int) -> None:
        self.time = time
        self.energy = energy
        self.row = row
        self.col = col

    def __lt__(self, other) -> bool:
        """The '<' operator is defined by least time. 
        If time is equal, least energy is taken."""
        
        ans = False
        
        # Prioritize time
        if self.time < other.time:
            ans = True

        # If equal time, choose less energy
        elif (self.time == other.time) and \
            (self.energy <= other.energy):
            ans = True
            
        return ans

    def __str__(self) -> str:
        return f"({self.time}, {self.energy}, {self.row}, {self.col})"


def calc_energy(h1: int, h2: int) -> int:
    """Calculate the required energy to move from h1 height to h2 height"""
    ans = g
    if h1 > h2:
        ans += ceil(a1 * (h1 - h2))
    elif h1 < h2:
        ans += ceil(a2 * (h2 - h1))
    return ans


def calc_time(h1: int, h2: int) -> int:
    """Calculate the required time to move from h1 height to h2 height"""
    ans = d
    if h1 > h2:
        ans += ceil(b1 * (h1 - h2))
    elif h1 < h2:
        ans += ceil(b2 * (h2 - h1))
    return ans


def solve(board: list, visited: list, M: int, N: int, 
          start: list, finish: list, E: int) -> int:
    """ 
    Function that solves the Bumpy Robot problem. 
    This algorithm is an implementation of Dijkstra's algorithm that searches for 
    the shortest path (in terms of time wasted) from an origin to a destination,
    using a heap as a priority queue

    Parameters
    ----------
    board : list
        A matrix of integers which represents the board of the problem.
     
    visited : list
        A matrix of integers that saves the least energy required to get 
        to the positions of the board from the starting position.

    M : int
        The amount of rows of the board.

    N : int
        The amount of columns of the board.
    
    start : list
        A list of two integers [rs, cs] which has the starting 
        position of the board.

    finish : list
        A list of two integers [rf, cf] which has the finish 
        position of the board.

    E : int
        The maximum amount of energy that can be wasted to get to 
        any position of the board.

    Returns
    -------
    int
        The minimum amount of time required to get to board[rf][cf] from
        board[rs][cs] using at most E units of energy.
        If no solution is found, returns -1.
      
    """          
              
    ans = -1
              
    # Set all positions as invalid
    for i in range(M):
        for j in range(N):
            visited[i][j] = 201

    # Start with no time wasted, and no energy wasted
    heap = [State(0, 0, start[0], start[1])]
    found = False
    
    # Guaranteed to end because energy wasted is always at least 1
    while len(heap) > 0 and not found: 
        state : State = heappop(heap)

        # If arrived to destination, then finish
        if state.row == finish[0] and state.col == finish[1]:
            found = True
            ans = state.time

        # If can move to board[row][col] with less energy
        elif state.energy < visited[state.row][state.col]:
            visited[state.row][state.col] = state.energy
            
            for k in range(4):
                # Calculate next movement on the board
                nxtRow = state.row + changeRow[k]
                nxtCol = state.col + changeCol[k]

                # Must be inside the board
                if nxtRow >= 0 and nxtRow < M and \
                   nxtCol >= 0 and nxtCol < N:

                    # Time and energy calculations
                    h1 = board[state.row][state.col]
                    h2 = board[nxtRow][nxtCol]
                    energy = calc_energy(h1, h2) + state.energy
                    time = calc_time(h1, h2) + state.time

                    # Energy wasted cannot be greater than E
                    if energy <= E:
                        heappush(heap, State(time, energy, nxtRow, nxtCol)) 

    return ans


def main():
    """Process that receives the input and prints the output."""
    global a1, a2, g, b1, b2, d
    
    # Visited based on energy.
    visited = [[201 for _ in range(MAX_SIZE)] for _ in range(MAX_SIZE)]

    # (row, column) for start and finish location
    start = [0, 0]
    finish = [0, 0]
    
    M, N = map(int, stdin.readline().split())
    while M > 0:
        a1, a2, g = map(float, stdin.readline().split())
        b1, b2, d = map(float, stdin.readline().split())
        g = int(g)
        d = int(d)

        board = [list(map(int, stdin.readline().split())) for _ in range(M)]
            
        start[0], start[1], finish[0], finish[1], E = list(map(lambda x: int(x) - 1, stdin.readline().split()))
        E += 1

        ans = solve(board, visited, M, N, start, finish, E)
        if ans == -1:
            print("failed")
        else:
            print(ans)
            
        M, N = map(int, stdin.readline().split())

        
main()
