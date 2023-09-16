using namespace std;

#include <string>
#include <queue>
#include <stack>
#include <vector>
#include <iostream>

bool needToContinue(queue<int> veue[], int size, stack<int> carrier)
{
    bool check = false;
    if(carrier.size() > 0)
    {
        return true;
    }
    else
    {
        for(int i = 0; i < size; i++)
        {
            check = check || (veue[i].size() != 0);
        }
        return check;
    }
}

int main()
{
    int cases, n, maxS, maxQ, Qi, elem, iter;
    int curr;
    bool next;
    string line;
    int minutes = -2;
    //vector<queue<int>> veue;
    queue<int> veue[100];
    stack<int> carrier;
    cin >> cases;
    while(cases--)
    {
        cin >> n >> maxS >> maxQ;
        for(int i = 0; i < n; i++)
        {
            cin >> Qi;
            //veue.push_back(queue<int>());
            veue[i] = queue<int>();
            for(int j = 0; j < Qi; j++)
            {
                cin >> elem;
                veue[i].push(elem);
            }
        }
        iter = 0;
        while(needToContinue(veue, n, carrier))
        {
            minutes += 2;
            next = false;
            //ciclo de descarga
            while(!next)
            {
                if(!carrier.empty())
                {
                    curr = carrier.top();
                    //Si se puede poner en la plataforma A
                    if(curr == iter + 1)
                    {
                        carrier.pop();
                        minutes++;
                    }
                    //Si se puede poner en la plataforma B
                    else if(veue[iter].size() < maxQ)
                    {
                        veue[iter].push(curr);
                        carrier.pop();
                        minutes++;
                    }
                    //Si no se puede en ninguna se pasa a cargar
                    else
                    {
                        next = true;
                    }
                }
                //Si el carrier esta vacio entonces se pasa a cargar
                else
                {
                    next = true;
                }
            }
            next = false;
            //ciclo de carga
            while(!next)
            {
                //Si hay elementos en la cola se intentan cargar
                if(!veue[iter].empty())
                {
                    curr = veue[iter].front();
                    //Si hay espacio en el carrier se pone
                    if(carrier.size() < maxS)
                    {
                        carrier.push(curr);
                        veue[iter].pop();
                        minutes++;
                    }
                    else
                    {
                        next = true;
                    }
                }
                else
                {
                    next = true;
                }
            }
            iter++;
            if(iter == n)
            {
                iter = 0;
            }
        }
        cout << minutes << endl;
        minutes = -2;
    }
    return 0;
}