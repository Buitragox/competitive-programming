//Made by Jhoan Buitrago 12/06/2021 dd/mm/aaaa

//Works just fine :)


#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

const int MAXN = 1030000;

vector<pair<int, int>> tree(MAXN * 2);
vector<char> pend(MAXN * 2, '$');

void reset()
{
    for(int i = 0; i < MAXN * 2; i++)
    {
        pend[i] = '$';
    }
}

pair<int, int> invValue()
{
    return make_pair(0, 0);
}

pair<int, int> createValue(int val)
{
    if(val == '0') 
        return make_pair(0, 1);
    else 
        return make_pair(1, 0);
}

pair<int, int> combine(pair<int, int> p1, pair<int, int> p2)
{
    return make_pair(p1.first + p2.first, p1.second + p2.second);
}

void selectLetter(int v, char letter)
{
    if (letter == 'F' || letter == 'E')
        pend[v] = letter;
    else if (letter == 'I')
    {
        if (pend[v] == 'I')
            pend[v] = '$';

        else if (pend[v] == 'F')
            pend[v] = 'E';
       
        else if (pend[v] == 'E')
            pend[v] = 'F';
        
        else if (pend[v] == '$')
            pend[v] = 'I';
    }
}

void change(int v, char letter)
{
    
    pair<int, int> ans = tree[v];
    if (letter == 'F')
    {
        ans.first += ans.second;
        ans.second = 0;
    }
    else if (letter == 'E')
    {
        ans.second += ans.first;
        ans.first = 0;
    }
    else if (letter == 'I')
    {
        int tmp = ans.first;
        ans.first = ans.second;
        ans.second = tmp;
    }
    tree[v] = ans;
}

void push(int v, int v1, int v2)
{
    selectLetter(v1, pend[v]);
    selectLetter(v2, pend[v]);
    change(v1, pend[v]);
    change(v2, pend[v]);
    
    pend[v] = '$';
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

void update(int v, int L, int R, int l, int r, char letter)
{
    if(l <= r)
    {
        if(l == L && r == R)
        {
            selectLetter(v, letter);
            change(v, letter);
            
        }
        else
        {
            int mid = L + ((R - L) >> 1);
            push(v, v + 1, v + 2 * (mid - L + 1));
            update(v + 1, L, mid, l, min(r, mid), letter);
            update(v + 2 * (mid - L + 1), mid + 1, R, max(l, mid + 1), r, letter);
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
    char letter;
    cin >> cases;
    while(cases--)
    {
        if(count != -1)
        {
            reset();
        }
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
            cin >> letter >> left >> right;
            if(letter == 'S')
            {
                ans = query(0, 0, last, left, right).first;
                cout << "Q" << countGod++ << ": " << ans << "\n";
            }
            else
            {
                update(0, 0, last, left, right, letter);
            }
        }
    }
    return 0;
}