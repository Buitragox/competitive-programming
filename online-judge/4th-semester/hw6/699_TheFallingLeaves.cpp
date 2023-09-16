#include <iostream>

using namespace std;

const int maxLength = 300;

int leaves[maxLength];

void reset()
{
    for(int i = 0; i < maxLength; i++)
    {
        leaves[i] = 0;
    }
}

void solve(int index)
{
    int value;
    cin >> value;
    if(value != -1)
    {
        leaves[index] += value;
        solve(index - 1);
        solve(index + 1); 
    }
}

int main()
{
    std::ios_base::sync_with_stdio(false);
    int root, i, value, cases = 1;
    int mid = maxLength / 2;
    cin >> root;
    while(root != -1)
    {
        reset();
        leaves[mid] = root;
        solve(mid - 1);
        solve(mid + 1);

        i = 0;
        value = leaves[0];
        while(value == 0)
        {
            i++;
            value = leaves[i];
        }
        cout << "Case " << cases++ << ":" << endl;
        while(value != 0)
        {
            cout << value;
            i++;
            value = leaves[i];
            if(value != 0)
            {
                cout << " ";
            }
        }
        cout << "\n\n";
        cin >> root;
    }

    return 0;
}