#include <iostream>
#include <vector>
#include <set>

using namespace std;

vector<pair<int, int>> processed; 
set<pair<int, int>> dEdges;
vector<vector<int>> graph;
int visited[1002];
int low[1002];
int father[1002];
int n, discTime = 0;

bool search(pair<int, int> p)
{
    for(int i = 0; i < processed.size(); i++)
    {
        if(processed[i].first == p.first && processed[i].second == p.second)
        {
            return true;
        }
    }
    return false;
}

// void bridgesAux(int node)
// {
//     int adjNode;
//     pair<int, int> p;
//     discTime ++;
//     visited[node] = discTime;
//     low[node] = discTime;

//     for(int i = 0; i < graph[node].size(); i++)
//     {
//         adjNode = graph[node][i];
//         p = make_pair(min(node, adjNode), max(node, adjNode));

//         if(!search(p))
//         {
//             processed.push_back(p);
            
//             if (visited[adjNode] == -1)
//             {
//                 father[adjNode] = node;
//                 bridgesAux(adjNode);
//                 low[node] = min(low[node], low[adjNode]);

//                 // Verificar si es un puente
//                 // añado el opuesto
//                 if(low[adjNode] > visited[node])
//                 {
//                     dEdges.insert(make_pair(adjNode, node));
//                 }
//             }
//             // back-edge
//             else if(adjNode != father[node])
//             {
//                 low[node] = min(low[node], visited[adjNode]);
//             }
            
//             // añado el normal
//             dEdges.insert(make_pair(node, adjNode));
//         }
//     }
// }

void bridgesAux(int node)
{
    int adjNode, tmp;
    discTime++;
    visited[node] = discTime;
    low[node] = discTime;

    for(int i = 0; i < graph[node].size(); i++)
    {
        adjNode = graph[node][i];

        if (visited[adjNode] == -1)
        {
            father[adjNode] = node;
            bridgesAux(adjNode);
            low[node] = min(low[node], low[adjNode]);
            
            // Verificar si es un puente
            // añado el opuesto
            if(low[adjNode] > visited[node])
            {
                dEdges.insert(make_pair(adjNode, node));
            }
            dEdges.insert(make_pair(node, adjNode));
            
        }
        // back-edge
        else if(adjNode != father[node])
        {
            tmp = low[node];
            low[node] = min(low[node], visited[adjNode]);
            if(low[node] != tmp)
            {
                //cout << node + 1 << " " << adjNode + 1 << endl;
                dEdges.insert(make_pair(node, adjNode));
            }

        }
    }
}


void bridges()
{
    for(int i = 0; i < n; i++)
    {
        if(visited[i] == -1)
        {
            bridgesAux(i);
        }
    }  
}



int main()
{
    int m, a, b, count = 1;
    cin >> n >> m;
    while(n != 0)
    {
        processed.clear();
        dEdges.clear();
        graph.clear();
        discTime = 0;
        for(int i = 0; i < n; i++)
        {
            graph.push_back(vector<int>());
            visited[i] = -1;
            father[i] = -1;
            low[i] = -1;
        }

        for(int i = 0; i < m; i++)
        {
            cin >> a >> b;
            graph[a - 1].push_back(b - 1);
            graph[b - 1].push_back(a - 1);
        }

        bridges();

        cout << count << "\n" << endl;
        for(set<pair<int, int>>::iterator it = dEdges.begin(); it != dEdges.end(); it++)
        {
            printf("%d %d\n", it->first + 1, it->second + 1);
        }
        cout << "#" << endl;
        cin >> n >> m;

        count ++;
    }
}      
