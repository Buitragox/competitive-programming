using namespace std;

#include <iostream>

int main()
{
    int cases, d, searched, node;
    cin >> cases;
    while(cases--)
    {
        cin >> d >> searched;
        node = 1;
        for(int i = 0; i < d - 1; i++)
        {
            if(searched % 2 == 0)
            {
                node = node * 2 + 1;
                searched /= 2;
            }
            else
            {
                node *= 2;
                searched = searched / 2 + 1;
            }
        }
        cout << node << endl;
    }
    return 0;
}
