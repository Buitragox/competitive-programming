#include <iostream>
#include <vector>
#include <queue>
#include <climits>

using namespace std;

int n;
vector<vector<pair<int, int>>> graph;
// vector<int> p(105);
// vector<int> d(105);
// vector<bool> inQueue(105);
// vector<int> count(105);
int p[105];
int d[105];
bool inQueue[105];
int count[105];

void initialize(int start){
	for(int i = 0; i < n; i++)
	{
		d[i] = INT_MAX;
		p[i] = -1;
		inQueue[i] = false;
		count[i] = 0;
	}

  	d[start] = 0;
}

bool bellmanFordOpt(int start)
{
	int node, adjNode, weight;
	queue<int> bfQueue;
	
	initialize(start);
	bfQueue.push(start);
	inQueue[start] = true;
	
	while(!bfQueue.empty()){
		node = bfQueue.front();
		bfQueue.pop();
		inQueue[node] = false;

		for(int i = 0; i < graph[node].size(); i++)
		{
			adjNode = graph[node][i].first;
			weight = graph[node][i].second;
			if(d[node] != INT_MAX && d[node] + weight < d[adjNode])
            {
                d[adjNode] = d[node] + weight;
                p[adjNode] = node;
				if(!inQueue[adjNode])
				{
					bfQueue.push(adjNode);
					inQueue[adjNode] = true;
					count[adjNode]++;

					//verifica si encontro un ciclo negativo
					if(count[adjNode] > n)
						return false;
				}
			}
		}
	}

  	return true;
}

int main()
{
    int boxes, a, b, w;
    cin >> n >> boxes;
    while(n != 0)
    {
        for(int i = 0; i < n; i++)
        {
            graph.push_back(vector<pair<int, int>>());
        }
        for(int i = 0; i < boxes; i++)
        {
            cin >> a >> b >> w;
            graph[a - 1].push_back(make_pair(b - 1, w));
            graph[b - 1].push_back(make_pair(a - 1, -w));  
        }
        if(bellmanFordOpt(0))
        {
            cout << "N" << endl;
        }
        else
        {
            cout << "Y" << endl;
        }
        
        cin >> n >> boxes;
        graph.clear();
    }
    return 0;
}