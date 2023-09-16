#include <iostream>
#include <vector>
#include <climits>
#include <algorithm>

using namespace std;

int n;

int count(vector<int> arr, int pos)
{
    int ans = 1;
    int elem = arr[pos];
    //contar a la izquierda
    for(int i = pos - 1; i >= 0; i--)
    {
        if(arr[i] == elem)
        {
            ans++;
        }
        else
        {
            break;
        }
        
    }
    //contar a la derecha
    for(int i = pos + 1; i <= n; i++)
    {
        if(arr[i] == elem)
        {
            ans++;
        }
        else
        {
            break;
        }
    }
    return ans;
}


pair<int, int> combine(vector<int> arr, pair<int, int> p1, pair<int, int> p2)
{
    pair<int, int> ans;
    //si son el mismo elemento sumo las frecuencias
    if(arr[p1.first] == arr[p2.first])
    {
        ans.first = p1.first;
        ans.second = p1.second + p2.second;
    }
    //si p1 es más común que p2
    else if(p1.second > p2.second)
    {
        ans.first = p1.first;
        ans.second = p1.second;
    }
    else if(p2.second > p1.second)
    {
        ans.first = p2.first;
        ans.second = p2.second;
    }
    else
    {
        //si p1 es menos común que p2 entonces p2 es la respuesta
        if(count(arr, p1.first) < count(arr, p2.first))
        {   
            ans.first = p2.first;
            ans.second = p2.second;
        }
        //de lo contrario p1 es la respuesta
        else
        {
            ans.first = p1.first;
            ans.second = p1.second;
        }
        
    }
    return ans;
}

void build(vector<pair<int, int>> &tree, vector<int> arr, int pos, int left, int right)
{
    if(left == right)
    {
        tree[pos] = make_pair(left, 1);
    }
    else
    {
        int mid = left + ((right - left) >> 1);
        build(tree, arr, pos + 1, left, mid);
        build(tree, arr, pos + 2 * (mid - left + 1), mid + 1, right);
        tree[pos] = combine(arr, tree[pos + 1], tree[pos + 2 * (mid - left + 1)]);
    }
}

pair<int, int> query(vector<pair<int, int>> tree, vector<int> arr, int pos, int L, int R, int l, int r)
{
    pair<int, int> ans;
    if(l > r)
    {
        ans = make_pair(INT_MIN, 0);
    }
    else if(l == L && r == R)
    {
        ans = tree[pos];
    }
    else
    {
        int mid = L + ((R - L) >> 1);
        pair<int, int> p1 = query(tree, arr, pos + 1, L, mid, l, min(r, mid));
        pair<int, int> p2 = query(tree, arr, pos + 2 * (mid - L + 1), mid + 1, R, max(l, mid + 1), r);
        ans = combine(arr, p1, p2);
    }
    return ans;
    
}

int main()
{
    int queries, number, left, right;
    pair<int, int> resPair;
    scanf("%d", &n);
    while(n > 0)
    {  
        vector<int> numbArray; 
        vector<pair<int, int>> tree(n * 2);
        scanf("%d", &queries);
        for(int i = 0; i < n; i++)
        {
            scanf("%d", &number);
            numbArray.push_back(number);
        }
        build(tree, numbArray, 0, 0, n - 1);
        for(int i = 0; i < n * 2; i++)
        {
            printf("(%d, %d) ", numbArray[tree[i].first], tree[i].second);
        }
        cout << endl;
        cout << "hello" << endl;
        for(int i = 0; i < queries; i++)
        {
            scanf("%d%d", &left, &right);
            cout << "oh no?" << endl;
            resPair = query(tree, numbArray, 0, 0, n - 1, left - 1, right - 1);
            cout << "ol gut" << endl;
            cout << resPair.second << endl;
        }
        scanf("%d", &n);
    }
    
    return 0;
}