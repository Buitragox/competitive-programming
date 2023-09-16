using namespace std;

#include <iostream>
#include <vector>
#include <limits>

vector<vector<pair<int, int>>> adj(502);
bool visited[502];
int MAX = numeric_limits<int>::lowest();
int n; 
int myCount = 0;

void dfsAux(int node)
{
    int adjNode, w;
    visited[node] = true;

    for(int i = 0; i < adj[node].size(); i++)
    {
        adjNode = adj[node][i].first;
        w = adj[node][i].second;
        if(!visited[adjNode] && w == MAX)
        {
            myCount++;
            dfsAux(adjNode);
        }
    }
}

int dfs()
{
    int maxCount = 0;
    for(int i = 0; i < n; i++)
    {
        visited[i] = false;
    }
    
    for(int i = 0; i < n; i++)
    {
        if(!visited[i])
        {
            myCount = 1;
            dfsAux(i);
            maxCount = max(maxCount, myCount);
        }
    }
    return maxCount;
}

int main()
{
    int routes, maxCount;
    int a, b, w;
    cin >> n >> routes;
    while(n != 0)
    {
        for(int i = 0; i < n; i++)
        {
            adj.push_back(vector<pair<int, int>>());
            visited[i] = false;
        }
        for(int i = 0; i < routes; i++)
        {
            cin >> a >> b >> w;
            adj[a - 1].push_back(make_pair(b - 1, w));
            adj[b - 1].push_back(make_pair(a - 1, w));
            MAX = max(MAX, w);
        }
        maxCount = dfs();
        cout << maxCount << endl;
        cin >> n >> routes;
        MAX = numeric_limits<int>::lowest();
        adj.clear();
    }
    return 0;
}