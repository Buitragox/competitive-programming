#include <vector>
#include <map>
#include <string>
#include <cstdio>
#include <iostream>
#define MAX 100002
//using namespace std;
using std::vector, std::cin, std::cout, std::endl;

bool visited[MAX];
int n;
int count = 0;
vector<vector<int>> adj(MAX);
vector<int> topo;

void topoSortAux(int node)
{
	int adjNode;
	visited[node] = true;

	for(int i = 0; i < adj[node].size(); i++)
	{
		adjNode = adj[node][i];
		if(!visited[adjNode])
		{
			topoSortAux(adjNode);
		}
	}
	topo.push_back(node);
}

void topoSort(){
	for(int i = 0; i < n; i++)
	{
		visited[i] = false;
	}
	
	for(int i = 0; i < n; i++)
	{
		if(!visited[i])
		{
			topoSortAux(i);
		}
	}
}

void dfsAux(int node){
	int adjNode;
	visited[node] = true;

	for(int i = 0; i < adj[node].size(); i++)
	{
		adjNode = adj[node][i];
		if(!visited[adjNode])
		{
			dfsAux(adjNode);
		}
	}
}

void dfs(){
	for(int i = 0; i < n; i++){
		visited[i] = 0;
	}
	int node;
	for(int i = n - 1; i >= 0; i--)
	{
		node = topo[i];
		if(!visited[node])
		{
			dfsAux(node);
			count++;
		}
	}
}

int main(){
	int m, node, adjNode;
	int cases;
	cin >> cases;
	while(cases--)
	{
		cin >> n >> m;
		count = 0;
        for(int i = 0; i < n; i++)
        {
            adj.push_back(vector<int>());
            visited[i] = 0; 
        }
		for(int i = 0; i < m; i++)
        {
            cin >> node >> adjNode;
            adj[node - 1].push_back(adjNode - 1);
        }
		topoSort();
		dfs();
		cout << count << endl;
		adj.clear();
		topo.clear();
	}
	

	return 0;
}
