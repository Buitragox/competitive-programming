#include <iostream>
#include <string>

using namespace std;

const int MAXN = 200100;

int arr[MAXN];
int tree[MAXN * 2];

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
        tree[pos] = tree[pos + 1] + tree[pos + 2 * (mid - left + 1)];
    }
}

int query(int pos, int L, int R, int l, int r)
{
    int ans;
    if(l > r)
    {
        ans = 0;
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
        ans = p1 + p2;
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
        tree[pos] = tree[pos + 1] + tree[pos + 2 * (mid - L + 1)];
    }  
}

int main()

{
    std::ios_base::sync_with_stdio(false);
    int n, aux1, aux2, cases = 1, ans;
    string input = "";
    cin >> n;
    
    while(n != 0)
    {
        for(int i = 0; i < n; i++)
        {
            cin >> arr[i];
        }
        build(0, 0, n - 1);
        cin >> input;
        cout << "Case " << cases++ << ":" << endl; 
        while(input != "END")
        {
            cin >> aux1 >> aux2;
            if(input == "M")
            {
                ans = query(0, 0, n - 1, aux1 - 1, aux2 - 1);
                cout << ans << "\n";
            }
            else
            {
                update(0, 0, n - 1, aux1 - 1, aux2);
            }
            cin >> input;
        }
        
        cin >> n;
        if(n != 0)
        {
            cout << "\n";
        }
    }
    return 0;
}