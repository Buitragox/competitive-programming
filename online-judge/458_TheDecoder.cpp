// Made by Jhoan Buitrago 01/10/2021
//                        dd/mm/aaaa

// Problem: https://onlinejudge.org/external/4/458.pdf

#include <iostream>
#include <string>

using namespace std;

int main()
{
    string input;
    while(cin >> input)
    {
        for(int i = 0; i < input.size(); i++)
        {
            input[i] -= 7; //We only need to substract 7 to the ascii code.
        }
        cout << input << endl;
    }
    return 0;
}