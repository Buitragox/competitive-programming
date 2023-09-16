#include <iostream>
#include <map>
#include <unordered_map>
#include <vector>
#include <set>
#include <queue>

using namespace std;

bool bfsAux(unordered_map<int, vector<int>> &tree, unordered_map<int, bool> &visited, int v)
{
    int u, w;
    bool isTree = true;
    queue<int> bfsQueue;
    visited[v] = true;
    bfsQueue.push(v);
    //cout << "doing bfs" << endl;
    while(!bfsQueue.empty() && isTree)
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
                visited[w] = true;
                bfsQueue.push(w);
            }
            else
            {
                //cout << "Found already visited: " << w << endl; 
                isTree = false;
                break;
            }
                
        }
    }
    return isTree;
}

bool bfs(unordered_map<int, vector<int>> &tree, 
        unordered_map<int, bool> &visited, set<int> &keys, 
        unordered_map<int, int> conections)
{
    int value;
    bool isTree = false;
    for(set<int>::iterator it = keys.begin(); it != keys.end(); it++)
    {
        int value = *it;
        if(conections[value] == 0)
        {
            //cout << "Value bfs is " << value << endl;
            isTree = bfsAux(tree, visited, value);
            break;
        }
    }
    for(set<int>::iterator it = keys.begin(); it != keys.end(); it++)
    {
        int value = *it;
        if(!visited[value])
        {
            //cout << "Found not visited: " << value << endl; 
            isTree = false;
            break;
        }
    }
    return isTree;
}

int main()
{
    std::ios_base::sync_with_stdio(false);
    int src = 1, dst = 1, cases = 1;
    bool enter;
    cin >> src >> dst;
    while(src >= 0)
    {
        enter = false;
        unordered_map<int, vector<int>> tree = unordered_map<int, vector<int>>();
        unordered_map<int, int> conections = unordered_map<int, int>();
        unordered_map<int, bool> visited = unordered_map<int, bool>();
        set<int> keys = set<int>();
        while(src > 0 && dst > 0)
        {
            //cout << "Read: " << src << " " << dst << endl;
            enter = true;
            tree[src].push_back(dst);
            //cout << tree[src][0] << endl;
            visited[src] = false;
            visited[dst] = false;
            tree[dst];
            keys.insert(src);
            keys.insert(dst);
            if(conections.find(src) == conections.end())
            {
                conections[src] = 0;
            }

            if(conections.find(dst) == conections.end())
            {
                conections[dst] = 1;
            }
            else
            {
                conections[dst]++;   
            }

            cin >> src >> dst;
        }
        //cout << "Keys" << endl;
        // for(set<int>::iterator it = keys.begin(); it != keys.end(); it++)
        // {
        //     cout << *it << endl;
        // }
        //cout << "End Keys" << endl;
        if(!enter)
        { 
            cout << "Case " << cases++ << " is a tree.\n";
        }
        else
        {
            if(bfs(tree, visited, keys, conections))
            {
                cout << "Case " << cases++ << " is a tree.\n";
            }
            else
            {
                cout << "Case " << cases++ << " is not a tree.\n";
            }
        }

        cin >> src >> dst;
    }
    return 0;
}