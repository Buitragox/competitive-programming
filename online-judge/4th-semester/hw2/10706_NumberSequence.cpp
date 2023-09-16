using namespace std;

#include <iostream>
#include <string>
#include <cmath>

const int MAX = 32001;
long long seq[MAX];

void makeSequence()
{
    long long Ak = 0;
    long long Sj = 1;
    for(int k = 1; k < MAX; k++)
    {
        Ak = Ak + Sj;
        Sj = Sj + floor(log10(k + 1)) + 1;
        seq[k] = Ak; 
    }
}

void findKSeq(int k)
{
    int low = 1;
    int hi = MAX;
    int mid;
    while(low + 1 != hi)
    {
        mid = (low + hi)/2;
        if(seq[mid] < k)
        {
            low = mid;
        }
        else
        {
            hi = mid;
        }
        
    }
    string Sk = "";
    for(int i = 1; i <= hi; i++)
    {
        Sk.append(to_string(i));
    }
    int ind;
    ind = k - (seq[hi] - Sk.length()) - 1;
    if(ind == -1)
    {
        ind = Sk.length() - 1;
    }
    if(k != 1)
    {
        cout << Sk[ind] << endl;
    }
    else
    {
        cout << 1 << endl;
    }
    
}


int main()
{
    makeSequence();
    int cases;
    int i;
    cin >> cases;
    while(cases--)
    {
        cin >> i;
        findKSeq(i);
    }
    return 0;
}