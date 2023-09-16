using namespace std;

#include <list>
#include <string>
#include <cstdio>
#include <iostream>

int main()
{
    int i;
    string line;
    string::iterator itLine;
    list<char> result;
    list<char>::iterator itRes;
    while(cin >> line)
    {
        cout << line << endl;
        result.clear();
        itRes = result.begin();
        for(itLine = line.begin(); itLine != line.end(); itLine++)
        {
            if(*itLine == '[')
            {
                itRes = result.begin();
            }
            else if(*itLine == ']')
            {
                itRes = result.end();
            }
            else if(*itLine != '\n')
            {
                if(itRes == result.end())
                {
                    result.push_back(*itLine);
                }
                else
                {
                    result.insert(itRes, *itLine);
                }
            }
        }
        for(itRes = result.begin(); itRes != result.end(); itRes++)
        {
            cout << *itRes;;
        }
        cout << "\n";
    }
    return 0;
}