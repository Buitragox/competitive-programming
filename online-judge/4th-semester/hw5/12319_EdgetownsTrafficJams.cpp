#include <iostream>
#include <vector>
#include <climits>
#include <string>
#include <sstream>

using namespace std;

int n;
int oldGraph[105][105];
int newGraph[105][105];
int oldDist[105][105];
int newDist[105][105];
//int oldNext[105][105];
//int newNext[105][105];

void floydWarshall(int graph[105][105], int dist [105][105]
                    /*,int nextMatrix[105][105]*/)
{
    //Inicialización
    for(int i = 0; i < n; i++)
    {
        for(int j = 0; j < n; j++)
        {
            dist[i][j] = graph[i][j];
            //nextMatrix[i][j] = j;
        }
        dist[i][i] = 0;
        //nextMatrix[i][i] = i;
    }

    //caminos más cortos
    for(int k = 0; k < n; k++)
    {
        for(int i = 0; i < n; i++)
        {
            for(int j = 0; j < n; j++)
            {

                if(dist[i][k] != INT_MAX && dist[k][j] != INT_MAX &&
                    (dist[i][k] + dist[k][j] < dist[i][j]))
                {
                    dist[i][j] = dist[i][k] + dist[k][j];
                    //nextMatrix[i][j] = nextMatrix[i][k];
                }
            }
        }
    }
}

int main()
{
    string line;
    int node, adjNode, A, B;
    scanf("%d\n", &n);
    bool ans;
    while(n != 0)
    {
        for(int i = 0; i < n; i++)
        {
            for(int j = 0; j < n; j++)
            {
                oldGraph[i][j] = INT_MAX;
                newGraph[i][j] = INT_MAX; 
            }
        }
        
        for(int i = 0; i < n; i++)
        {
            getline(cin, line);
            //cout << "line: " << line << endl;
            stringstream input(line);
            input >> node;
            while(input >> adjNode)
            {
                oldGraph[node - 1][adjNode - 1] = 1;
            }
        }
        //cout << "new" << endl;
        for(int i = 0; i < n; i++)
        {
            getline(cin, line);
            //cout << "line: " << line << endl;
            stringstream input(line);
            input >> node;
            while(input >> adjNode)
            {
                newGraph[node - 1][adjNode - 1] = 1;
            }
        }
        cin >> A >> B;
        floydWarshall(oldGraph, oldDist);
        floydWarshall(newGraph, newDist);

        ans = true;
        for(int i = 0; i < n && ans; i++)
        {
            for(int j = 0; j < n && ans; j++)
            {
                if(newDist[i][j] > (A * oldDist[i][j] + B))
                {
                    ans = false;
                }
            }
        }
        if(ans)
        {
            cout << "Yes" << endl;
        }
        else
        {
            cout << "No" << endl;
        }
        scanf("%d\n", &n);
    }
}
