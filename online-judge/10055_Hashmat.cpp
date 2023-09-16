#include <iostream>

using namespace std;

int main()
{
    unsigned long int aux1, aux2;
    while(cin >> aux1 >> aux2)
    {
        if(aux1 > aux2)
        {
            cout << aux1 - aux2 << "\n";
        }
        else
        {
            cout << aux2 - aux1 << "\n";
        }
    } 
    return 0;
}