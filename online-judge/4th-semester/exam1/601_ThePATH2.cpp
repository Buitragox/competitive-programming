using namespace std;

#include <iostream>
#include <cstdio>
#include <vector>
#include <queue>

// 0 = nada, 1 = victoria en un movimiento
int whiteWin;
int blackWin;
bool visited[100][100];
char board[100][100];
int n;
int changeX[] = {-1, 0, 1, 0};
int changeY[] = {0, 1, 0, -1};

void dfsAux(int x, int y, char color)
{
    //printf("newX=%d, newY=%d\n", x, y);
    if(color == 'W' && y == n - 1 && whiteWin != 1)
    {
        whiteWin = 1;
    }
    else if(color == 'B' && x == n - 1 && blackWin != 1)
    {
        blackWin = 1;
    }

    visited[x][y] = true;
    int newX;
    int newY;
    for(int i = 0; i < 4; i++)
    {
        newX = x + changeX[i];
        newY = y + changeY[i];
        if(newX >= 0 && newY >= 0 && newX < n && newY < n)
        {
            if(board[newX][newY] == color && !visited[newX][newY])
            {
                dfsAux(newX, newY, color);
            }
        }
    }
}

void cleanVisited()
{
    for(int i = 0; i < n; ++i)
    {
        for(int j = 0; j < n; j++)
        {
            visited[i][j] = false;
        }
    }
}

void dfs(char color)
{
    for(int i = 0; i < n; ++i)
    {
        if(color == 'W')
        {
            if(!visited[i][0] && board[i][0] == color)
            {
                dfsAux(i, 0, color);
            }
        }
        else if(color == 'B')
        {
            if(!visited[0][i] && board[0][i] == color)
            {
                dfsAux(0, i, color);
            }
        }
    }
}

int main()
{
    cin >> n;
    while(n != 0)
    {
        // board = vector<vector<char>>(n);
        // visited = vector<vector<bool>>(n);
        char line[100];
        for(int i = 0; i < n; i++)
        {
            // visited[i] = vector<bool>(n, false);
            //scanf("%s", line);
            cin >> line;
            for(int j = 0; j < n; j++)
            {
                board[i][j] = line[j];
            }
        }
        whiteWin = 0;
        blackWin = 0;
        cleanVisited();
        dfs('W');
        cleanVisited();
        dfs('B');
        if(whiteWin == 1)
        {
            cout << "White has a winning path." << endl;
        }
        else if(blackWin == 1)
        {
            cout << "Black has a winning path." << endl;
        }
        else
        {
            for(int i = 0; i < n; i++)
            {
                for(int j = 0; j < n; j++)
                {
                    if(board[i][j] == 'U')
                    {
                        //printf("found U at i=%d, j=%d\n", i, j);
                        cleanVisited();
                        board[i][j] = 'W';
                        dfs('W');
                        //cout << whiteWin << endl;
                        cleanVisited();
                        board[i][j] = 'B';
                        dfs('B');
                        board[i][j] = 'U';
                    }
                }
            }
            if(whiteWin == 1)
            {
                cout << "White can win in one move." << endl;
            }
            else if(blackWin == 1)
            {
                cout << "Black can win in one move." << endl;
            }
            else
            {
                cout << "There is no winning path." << endl;
            }
        }

        cin >> n;
    }
    return 0;
}