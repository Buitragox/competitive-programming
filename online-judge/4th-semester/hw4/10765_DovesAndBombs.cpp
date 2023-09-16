#include <iostream>
#include <vector>
#include <list>
#include <set>
#include <algorithm>

using namespace std;

int n, bombs, discTime;
vector<vector<int>> graph;
int visited[10002];
int low[10002];
int father[10002];
set<int> apNodes;
vector<pair<int, int>> stations;

bool compare(pair<int, int> p1, pair<int, int> p2)
{
    if(p1.second == p2.second)
    {
        return p1.first < p2.first;
    }
    else
    {
        return p1.second > p2.second;
    }
}

void apAux(int node)
{
    int adjNode, sons = 0;
    discTime++;
    visited[node] = discTime;
    low[node] = discTime;

    for(int i = 0; i < graph[node].size(); i++)
    {
        adjNode = graph[node][i];
        if(visited[adjNode] == -1)
        {
            sons++;
            father[adjNode] = node;
            apAux(adjNode);
            low[node] = min(low[node], low[adjNode]);

            //verificar si es un punto de articulacion
            if(father[node] != -1 && low[adjNode] >= visited[node])
            {
                apNodes.insert(node);
            }
        }
        // back-edge
        else if(adjNode != father[node])
        {
            low[node] = min(low[node], visited[adjNode]);
        } 
    }
    // root
    if(father[node] == -1 && sons > 1)
    {
        apNodes.insert(node);
    }
}

void ap()
{
    for(int i = 0; i < n; i++)
    {
        low[i] = -1;
        visited[i] = -1;
        father[i] = -1;
    }
        

    for(int i = 0; i < n; i++)
    {
        if(visited[i] == -1)
        {
            apAux(i);
        }
    }
}

void dfsAux(int node)
{
    int adjNode, w;
    visited[node] = true;
    for(int i = 0; i < graph[node].size(); i++)
    {
        adjNode = graph[node][i];
        if(!visited[adjNode])
        {
            dfsAux(adjNode);
        }
    }
}

void clearVis()
{
    for(int i = 0; i < n; i++)
    {
        visited[i] = 0;
    }
}

bool search(int node)
{
    for(set<int>::iterator it = apNodes.begin(); it != apNodes.end(); it++)
    {
        if(*it == node)
        {
            return true;
        }
    }
    return false;
}

void dfs()
{
    int count;
    for(set<int>::iterator it = apNodes.begin(); it != apNodes.end(); it++)
    {
        count = 0;
        clearVis();
        visited[*it] = 1;
        for(int i = 0; i < n; i++)
        {
            if(!visited[i])
            {
                count++;
                dfsAux(i);
            }
        }
        stations.push_back(make_pair(*it, count));
    }
    int fill = bombs - stations.size();
    for(int i = 0; i < n && fill > 0; i++)
    {
        if(!search(i))
        {
            stations.push_back(make_pair(i, 1));
            fill--;
        }
    }
}

int main()
{
    int a, b;
    cin >> n >> bombs;
    while(n != 0)
    {
        for(int i = 0; i < n; i++)
        {
            graph.push_back(vector<int>());
            visited[i] = false;
        }
        cin >> a >> b;
        while(a != -1)
        {
            graph[a].push_back(b);
            graph[b].push_back(a);
            cin >> a >> b;
        }
        ap();
        dfs();
        sort(stations.begin(), stations.end(), compare);
        
        for(int i = 0; i < bombs; i++)
        {
            cout << stations[i].first << " " << stations[i].second << endl;
        }
        cout << endl;
        
        cin >> n >> bombs;
        graph.clear();
        apNodes.clear();
        stations.clear();
    }
    return 0;
}