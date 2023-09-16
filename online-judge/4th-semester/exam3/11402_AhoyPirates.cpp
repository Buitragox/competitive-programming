#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

const int MAXN = 1030000;

vector<pair<int, int>> tree(MAXN * 2);
vector<string> pend(MAXN * 2, "");

pair<int, int> invValue()
{
    return make_pair(0, 0);
}

pair<int, int> createValue(int val)
{
    if(val == '0') return make_pair(0, 1);
    else return make_pair(1, 0);
}

pair<int, int> combine(pair<int, int> p1, pair<int, int> p2)
{
    return make_pair(p1.first + p2.first, p1.second + p2.second);
}

pair<int, int> change(int v, string &str)
{
    int tmp;
    pair<int, int> ans = tree[v];
    for(int i = 0; i < str.size(); i++)
    {
        if (str[i] == 'F')
        {
            ans.first = ans.first + ans.second;
            ans.second = 0;
        }
        else if (str[i] == 'E')
        {
            ans.second = ans.first + ans.second;
            ans.first = 0;
        }
        else if (str[i] == 'I')
        {
            tmp = ans.first;
            ans.first = ans.second;
            ans.second = ans.first;
        }
    }
    return ans;
}

void push(int v, int v1, int v2)
{
    tree[v1] = change(v1, pend[v]);
    pend[v1] += pend[v];
    tree[v2] = change(v2, pend[v]);
    pend[v2] += pend[v];
    pend[v] = "";
}

void build(string &arr, int v, int l, int r)
{
    if(l == r)
    {
        tree[v] = createValue(arr[l]);
    }
    else
    {
        int mid = l + ((r - l) >> 1);
        build(arr, v + 1, l, mid);
        build(arr, v + 2 * (mid - l + 1), mid + 1, r);
        tree[v] = combine(tree[v + 1], tree[v + 2 * (mid - l + 1)]);
    }
}

pair<int, int> query(int v, int L, int R, int l, int r)
{
    pair<int, int> ans;
    if(l > r)
    {
        ans = invValue();
    }
    else if(l == L && r == R) 
    {
        ans = tree[v];
    }
    else
    {
        int m = L + ((R - L) >> 1);
        push(v, v + 1, v + 2 * (m - L + 1));
        ans = combine(query(v + 1, L, m, l, min(r, m)), 
                      query(v + 2 * (m - L + 1), m + 1, R, max(l, m + 1), r));

    }
    return ans;
}

void update(int v, int L, int R, int l, int r, string &h)
{
    if(l <= r)
    {
        if(l == L && r == R)
        {
            tree[v] = change(v, h);
            pend[v] += h;
        }
        else
        {
            int mid = L + ((R - L) >> 1);
            push(v, v + 1, v + 2 * (mid - L + 1));
            update(v + 1, L, mid, l, min(r, mid), h);
            update(v + 2 * (mid - L + 1), mid + 1, R, max(l, mid + 1), r, h);
            tree[v] = combine(tree[v + 1], tree[v + 2 * (mid - L + 1)]);
        }
    }
}


int main()
{
    std::ios_base::sync_with_stdio(false);
    int cases, mPairs, mult, last, queries;
    int left, right, ans;
    int countGod, count;
    count = 1;
    string op;
    cin >> cases;
    while(cases--)
    {
        string arr = "";
        cin >> mPairs;
        while(mPairs--)
        {
            cin >> mult;
            cin >> op;
            for(int i = 0; i < mult; i++)
            {
                arr += op;
            }
        }
        last = arr.size() - 1;
        build(arr, 0, 0, last);
        countGod = 1;
        cin >> queries;
        cout << "Case " << count++ << ":\n";
        while(queries--)
        {
            cin >> op >> left >> right;
            if(op == "S")
            {
                ans = query(0, 0, last, left, right).first;
                cout << "Q" << countGod++ << ": " << ans << "\n";
            }
            else
            {
                update(0, 0, last, left, right, op);
            }
        }
    }
    return 0;
}