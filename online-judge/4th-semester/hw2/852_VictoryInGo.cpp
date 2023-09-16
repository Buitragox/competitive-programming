using namespace std;

#include <iostream>
#include <string>
#include <queue>

char board[9][9];
int blackPoints;
int whitePoints;
int changeX[] = {-1, 0, 1, 0};
int changeY[] = {0, 1, 0, -1};
int visited[9][9];
int tempPoints;

bool bfsTerritory(int posX, int posY, char Enemy)
{
    int newX, newY;
    pair<int, int> pos;
    bool check = true;
    queue<pair<int, int>> bfsQueue;
    bfsQueue.push(make_pair(posX, posY));
    visited[posX][posY] = 1;
    tempPoints = 1;
    while(!bfsQueue.empty())
    {
        pos = bfsQueue.front();
        bfsQueue.pop();
        for(int i = 0; i < 4; i++)
        {
            newX = pos.first + changeX[i];
            newY = pos.second + changeY[i];
            if(newX >= 0 && newY >= 0 && newX < 9 && newY < 9)
            {
                if(board[newX][newY] == Enemy)
                {
                    check = false;
                }
                else if(board[newX][newY] == '.' && !visited[newX][newY])
                {
                    bfsQueue.push(make_pair(newX, newY));
                    visited[newX][newY] = 1;
                    tempPoints++;
                }
            }
        }
    }
    return check;
}


void dfsAux(int posX, int posY, char color)
{
    int newX, newY;
    bool check;
    visited[posX][posY] = 1;
    if(color == 'X')
    {
        blackPoints++;
    }
    else
    {
        whitePoints++;
    }
    for(int i = 0; i < 4; i++)
    {
        newX = posX + changeX[i];
        newY = posY + changeY[i];
        if(newX >= 0 && newY >= 0 && newX < 9 && newY < 9 && !visited[newX][newY])
        {
            if(board[newX][newY] == color)
            {
                dfsAux(newX, newY, color);
            }
            else if(board[newX][newY] == '.' && !visited[newX][newY])
            {
                if(color == 'X')
                {
                    check = bfsTerritory(newX, newY, 'O');
                    blackPoints = check ? (blackPoints + tempPoints) : blackPoints;
                }
                else
                {
                    check = bfsTerritory(newX, newY, 'X');
                    whitePoints = check ? (whitePoints + tempPoints) : whitePoints;
                }
            }
        }
    }

}

void dfs()
{
    for(int i = 0; i < 9; i++)
    {
        for(int j = 0; j < 9; j++)
        {
            if(!visited[i][j] && board[i][j] == 'X')
            {
                dfsAux(i, j, 'X');
            }
        }
    }
    //printf("Negras %d\n", blackPoints);
    for(int i = 0; i < 9; i++)
    {
        for(int j = 0; j < 9; j++)
        {
            if(!visited[i][j] && board[i][j] == 'O')
            {
                dfsAux(i, j, 'O');
            }
        }
    }
    //printf("Blancas %d\n", whitePoints);

}

int main()
{
    int cases;
    cin >> cases;
    string line;
    while(cases--)
    {
        blackPoints = 0;
        whitePoints = 0;
        for(int i = 0; i < 9; i++)
        {
            cin >> line;
            for(int j = 0; j < 9; j++)
            {
                visited[i][j] = 0;
                board[i][j] = line[j];
                //cout << board[i][j];;
            }
            //cout << '\n';
        }
        dfs();
        cout << "Black " << blackPoints << " White " << whitePoints << endl;
        

    }
    return 0;
}