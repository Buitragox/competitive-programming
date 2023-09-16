#include <iostream>
#include <vector>
#include <queue>
#include <set>

using namespace std;

int n, maxRad, maxDia;
int incidence[5500];
int level[5500];
int visited[5500];

void bfsAux(vector<vector<int>> &tree, int v)
{
    int u, w;
    queue<int> bfsQueue;
    visited[v] = 1;
    bfsQueue.push(v);
    //cout << "doing bfs" << endl;
    while(!bfsQueue.empty())
    {
        u = bfsQueue.front();
        //cout << "  Im in" << u << endl;
        bfsQueue.pop();
        for(int i = 0; i < tree[u].size(); ++i)
        {
            w = tree[u][i];
            if(!visited[w])
            {
                //cout << "    visiting: " << w << endl; 
                visited[w] = visited[u] + 1;
                if(visited[w] > maxDia)
                {
                    maxDia = visited[w];
                }
                bfsQueue.push(w);
            }
                
        }
    }

}

set<int> bfs(vector<vector<int>> &tree, vector<int> &centerNodes)
{
    set<int> diameterNodes;
    
    for(int i = 0; i < centerNodes.size(); i++)
    {
        for(int i = 0; i < n; i++)
        {
            visited[i] = 0;
        }
        maxDia = 0;
        bfsAux(tree, centerNodes[i]);

        for(int i = 0; i < n; i++)
        {
            if(visited[i] == maxDia)
            {
                diameterNodes.insert(i);
            }
        }
    }
    return diameterNodes;
}

vector<int> center(vector<vector<int>> &tree){
    int v, rad;
    maxRad = 0;
    queue<int> cQueue;
    vector<int> centerNodes;

    // for(int i = 0; i < n; i++)
    // {
    //     for(int j = 0; j < tree[i].size(); j++)
    //     {
    //         cout << " " << tree[i][j];
    //     }
    //     cout << endl;
    // }

    for(int i = 0; i < n; i++)
    {
        level[i] = 0;
        incidence[i] = tree[i].size();
        //cout << "i " << i << " inc " << incidence[i] << endl;
    }

    for(int i = 0; i < n; i++)
    {
        if(incidence[i] == 1)
        {
            cQueue.push(i);
        }
    }
        
    while(!cQueue.empty())
    {
        v = cQueue.front();
        cQueue.pop();

        for(int i = 0; i < tree[v].size(); i++)
        {
            incidence[tree[v][i]]--;
            if(incidence[tree[v][i]] == 1)
            {
                cQueue.push(tree[v][i]);
                level[tree[v][i]] = level[v] + 1;
                maxRad = max(maxRad, level[tree[v][i]]);
            }
        }
    }

    for(int i = 0; i < n; i++)
    {
        if(level[i] == maxRad)
        {
            centerNodes.push_back(i);
        }
    }
        
    rad = (centerNodes.size() >= 2) ? maxRad + 1 : maxRad;
    return centerNodes;
}


int main()
{
    std::ios_base::sync_with_stdio(false);
    int amountEdges, aux;
    while(cin >> n)
    {
        vector<vector<int>> tree(n, vector<int>());
        for(int i = 0; i < n; i++)
        {
            cin >> amountEdges;
            //cout << "amountEdges " << amountEdges << endl;
            for(int j = 0; j < amountEdges; j++)
            {
                cin >> aux;
                //cout << aux << endl;
                tree[i].push_back(aux - 1);
                // tree[aux - 1].push_back(i);
            }
        }

        vector<int> centerNodes = center(tree);
        set<int> diameterNodes = bfs(tree, centerNodes);

        cout << "Best Roots  :";
        for(int i = 0; i < centerNodes.size(); i++)
        {
            cout << " " << centerNodes[i] + 1;
        }
        cout << "\n";

        cout << "Worst Roots :";
        for(set<int>::iterator it = diameterNodes.begin(); it != diameterNodes.end(); it++)
        {
            cout << " " << *it + 1;
        }
        cout << "\n";

    }
    return 0;
}