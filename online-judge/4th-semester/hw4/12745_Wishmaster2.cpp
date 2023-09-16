#include <iostream>
#include <vector>
#include <stack>
#include <map>
#include <algorithm>

// Pain

using namespace std;

int n, t;
int numSCC;
vector<vector<int>> graph;
// map<int, int> visited;
// map<int, int> low;
// map<int, bool> inStack;
int visited[200008];
int low[200008];
int inStack[200008];
stack<int> freeNodes; //nodos que todavía no tienen asignado un componente
//vector<vector<int>> sccNodes;

void tarjanAux(int node){
    int adjNode;
    t++;
    visited[node] = t;
    low[node] = t;
    freeNodes.push(node);
    inStack[node] = true;

    for(int i = 0; i < graph[node].size(); i++)
    {
        adjNode = graph[node][i];
        if(visited[adjNode] == -1)
        {
            tarjanAux(adjNode);
            low[node] = min(low[node], low[adjNode]);
        }
        else if(inStack[adjNode])
        {
            low[node] = min(low[node], visited[adjNode]);
        }   
        
    }
    if(low[node] == visited[node])
    {
        int top;
        //cout << "SCC con indice " << low[node] << ": ";
        //sccNodes.push_back(vector<int>());
        while(freeNodes.top() != node)
        {
            top = freeNodes.top();
            //cout << freeNodes.top() << " ";
            inStack[top] = false;
            low[top] = low[node];
            //sccNodes[numSCC].push_back(freeNodes.top());
            freeNodes.pop();
        }
        //cout << freeNodes.top() << endl;
        inStack[freeNodes.top()] = false;
        //sccNodes[numSCC].push_back(freeNodes.top());
        freeNodes.pop();
        numSCC++;
    }
}

void tarjan(){
    for(int i = 1; i <= n; i++)
    {
        low[i] = -1;
        low[i + n] = -1;
        visited[i] = -1;
        visited[i + n] = -1;
        inStack[i] = false;
        inStack[i + n] = false;
    }

    for(int i = 1; i <= n; i++)
    {
        if(visited[i] == -1)
        {
            tarjanAux(i);
        }
        if(visited[i + n] == -1)
        {
            tarjanAux(i + n);
        }
    }
}


int main()
{
    int cases, wishes, count = 1;
    int w1, w2, negw1, negw2;
    bool check;
    cin >> cases;
    while(cases--)
    {
        cin >> n >> wishes;
        for(int i = 1; i <= 2 * (n + 1); i++)
        {
            graph.push_back(vector<int>());
        }
        for(int i = 0; i < wishes; i++)
        {
            cin >> w1 >> w2;
            negw1 = w1 + n;
            negw2 = w2 + n;
            if(w1 < 0)
            {
                negw1 = -w1;
                w1 = -w1 + n;
            }
            if(w2 < 0)
            {
                negw2 = -w2;
                w2 = -w2 + n;
            }
            //cout << negw1 << " " << w2 << endl;
            //cout << negw2 << " " << w1 << endl;
            //cout << endl;
            graph[negw1].push_back(w2);
            graph[negw2].push_back(w1);
        }
        //Print graph
        // for(int i = 1; i <= n * 2; i++)
        // {
        //     cout << "Node " << i << ": ";
        //     for(int j = 0; j < graph[i].size(); j++)
        //     {
        //         cout << graph[i][j] << " ";
        //     }
        //     cout << endl;
        // }
        tarjan();
        check = true;

        for(int i = 1; i <= n; i++)
        {
            // printf("low %d = %d, low %d = %d\n", i, low[i], -i, low[-i]);
            if(low[i] == low[i + n])
            {
                check = false;
                break;
            }
        }
        printf("Case %d: %s\n", count, (check ? "Yes" : "No"));
        count++;
        graph.clear();
    }
}