/*
Implementacion Algoritmo de Dijkstra para SSSP
Autor: Carlos Ramirez
Fecha: Abril 25 de 2020

*/

#include <climits>
#include <vector>
#include <queue>
#include <iostream>

using namespace std;

int n;
vector<vector<pair<int, int> > > graph(50000);
int fuelPrice[1005];
vector<int> p(50000);
vector<int> d(50000);

struct State
{
    int node;
    int weight;
    int tank;
    State(int n, int w, int t)
    {
        node = n;
        weight = w;
        tank = t;
    }
};

class Comp
{
    public:
        bool operator() (const State& s1, const State& s2) const
        {
            return s1.weight > s2.weight;
        }
};

void initialize(int s){
    for(int i = 0; i < n; ++i)
    {
        d[i] = INT_MAX;
        p[i] = -1;
    }

    d[s] = 0;
}

void dijkstra(int s){
    int weight, node, adj, dist, tank, refuel, price;
    priority_queue<State, vector<State>, Comp> pQueue;
    
    initialize(s);
    pQueue.push(State(s, 0, 0));

    while(!pQueue.empty())
    {
        weight = pQueue.top().weight;
        node = pQueue.top().node;
        tank = pQueue.top().tank;
        pQueue.pop();
        for(int i = 0; i < graph[node].size(); i++)
        {
            adj = graph[node][i].first;
            dist = graph[node][i].second;
            if(tank < dist)
            {
                price = (dist - tank) * fuelPrice[node];
                if(weight + price < d[adj])
                {
                    d[adj] = weight + price;
                    //pQueue.push(State(adj, d[adj]))
                }
            }
        }   
            // for(int j = 0; j < graph[u].size(); ++j)
            // {
            //     v = graph[u][j].first;
            //     peso = graph[u][j].second;
            //     if(d[u] != INT_MAX && d[u] + peso < d[v])
            //     { 
            //         d[v] = d[u] + peso;
            //         p[v] = u;
            //         cola.push(make_pair(d[v], v));
            //     }
            // }
    }
}

int main()
{
    return 0;
}
