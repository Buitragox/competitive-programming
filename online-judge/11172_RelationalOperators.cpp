#include <iostream>

using namespace std;

int main()
{
    int cases;
    cin >> cases;
    long int a, b;
    while(cases--)
    {
        cin >> a >> b;
        if(a < b)
        {
            cout << "<";
        }
        else if(a == b)
        {
            cout << "=";
        }
        else
        {
            cout << ">";
        }
        cout << "\n";
    } 
    return 0;
}