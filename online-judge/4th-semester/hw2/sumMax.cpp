using namespace std;

#include <iostream>
#include <string>
#include <cmath>

const int MAX = 32001;
long long seq[MAX];
string Sk;
int main()
{
    long long Ak = 0;
    long long Sj = 1;
    int k;
    for(k = 1; k <= MAX; k++)
    {
        Ak = Ak + Sj;
        //cout << "Sj=" << Sj;
        Sj = Sj + floor(log10(k + 1)) + 1;
        seq[k] = Ak;
        //cout << " k=" << k << "   Ak=" << Ak << endl; 
    }
    cout << seq[k] << " " << Ak << endl;
    cout << "xd" << endl;
    return 0;
}