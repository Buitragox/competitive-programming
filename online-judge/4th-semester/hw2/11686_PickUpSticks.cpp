using namespace std;

#include <iostream>
#include <queue>

int n = 0;
vector<vector<int>> adj;
vector<int> inc;
vector<int> topo;

void kahnAlgorithm()
{
	queue<int> kahnQueue;
	// Primero agregamos los elementos que no tengan conexiones hacia ellos
	// es decir que su incidencia sea 0
	for(int i = 0; i < n; ++i)
	{
		if(inc[i] == 0)
		{
			kahnQueue.push(i);
		}	
	}
	
	int node, nodeAdj, vis = 0;
	// Se crea el orden topológico
	while(!kahnQueue.empty())
	{
		node = kahnQueue.front();
		kahnQueue.pop();
        topo.push_back(node);

		for(int i = 0; i < adj[node].size(); ++i)
		{
			nodeAdj = adj[node][i];
			--inc[nodeAdj];
			if(inc[nodeAdj] == 0)
			{
				kahnQueue.push(nodeAdj);
			}
		}
		vis++;
	}

	// Se verifica que todos los nodos hayan terminado con incidencia 0
	if(vis != n)
	{
		printf("IMPOSSIBLE\n");
	}
	else
	{
		for(int i = 0; i < n; i++)
		{
			cout << topo[i] + 1 << endl;
		}
	}
}

int main()
{
    int amountAdj, node, nodeAdj;
    int m;
    cin >> n >> m;
    while(n != 0 && m != 0)
    {
        adj = vector<vector<int>>(n);
        inc = vector<int>(n);
        topo = vector<int>();
        for(int i = 0; i < m; i++)
        {
            cin >> node >> nodeAdj;
            node--;
            nodeAdj--;
            adj[node].push_back(nodeAdj);
            inc[nodeAdj]++;
        }
        
        kahnAlgorithm();
        cin >> n >> m;
    }
    return 0;
}