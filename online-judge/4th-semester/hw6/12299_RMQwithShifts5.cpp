#include <iostream>
#include <vector>
#include <sstream>
#include <string>
#include <climits>

using namespace std;

int arr[100500];
int tree[210000];

void build(int pos, int left, int right)
{
    if(left == right)
    {
        tree[pos] = arr[left];
    }
    else
    {
        int mid = left + ((right - left) >> 1);
        build(pos + 1, left, mid);
        build(pos + 2 * (mid - left + 1), mid + 1, right);
        tree[pos] = min(tree[pos + 1], tree[pos + 2 * (mid - left + 1)]);
    }
}

int query(int pos, int L, int R, int l, int r)
{
    int ans;
    if(l > r)
    {
        ans = INT_MAX;
    }
    else if(l == L && r == R)
    {
        ans = tree[pos];
    }
    else
    {
        int mid = L + ((R - L) >> 1);
        int p1 = query(pos + 1, L, mid, l, min(r, mid));
        int p2 = query(pos + 2 * (mid - L + 1), mid + 1, R, max(l, mid + 1), r);
        ans = min(p1, p2);
    }
    return ans;
}

void update(int pos, int L, int R, int index, int elem)
{
    if(L == R)
    {
        tree[pos] = elem;
    }
    else
    {
        int mid = L + ((R - L) >> 1);
        if(index <= mid)
        {
            update(pos + 1, L, mid, index, elem);
        }
        else
        {
            update(pos + 2 * (mid - L + 1), mid + 1, R, index, elem);
        }
        tree[pos] = min(tree[pos + 1], tree[pos + 2 * (mid - L + 1)]);  
    }  
}

void swap(int i, int j)
{
    int temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
}

int main()
{
    std::ios_base::sync_with_stdio(false);
    int n, queries, aux;
    string input;
    char op, xd;
    cin >> n >> queries;
    int last = n - 1;
    for(int i = 0; i < n; i++)
    {
        cin >> aux;
        arr[i] = aux;
    }
    build(0, 0, last);
    for(int i = 0; i < queries; i++)
    {
        cin.ignore(1, '\n');
        vector<int> numbers;
        cin.get(op);
        //cout << op << "\n";
        for(int j = 0; j < 5; j++)
        {
            cin.get(xd);
        }

        do
        {
            cin >> aux >> xd;
            numbers.push_back(aux - 1);
        } while(xd != ')');       

        if(op == 'q')
        {
            cout << query(0, 0, last, numbers[0], numbers[1]) << '\n';
        }
        else
        {
            for(int k = 0; k < numbers.size() - 1; k++)
            {
                swap(numbers[k], numbers[k + 1]);
            }
            for(int k = 0; k < numbers.size(); k++)
            {
                update(0, 0, last, numbers[k], arr[numbers[k]]);
            }
            
        }
    }
    return 0;
}