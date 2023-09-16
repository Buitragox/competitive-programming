using namespace std;

#include <cmath>
#include <iostream>
#include <sstream>
#include <limits>

double f(double r, double Lp)
{
    return r * sqrt(2 * (1 - cos(Lp / r)));
}

int main()
{
    string left, right, s;
    double L, n, C, Lp;
    double low, hi, mid, r, ans, a;
    cin >> L >> n >> C;
    while(L >= 0)
    {
        Lp = (1 + n * C) * L;
        if(L != Lp)
        {
            low = 0.00001;
            hi = numeric_limits<int>::max();
            if(L < 1000)
            {
                hi = 10000000;
                
            }
            while(abs(L - f(low, Lp)) > 1e-8)
            {
                mid = (hi + low) / 2;

                if(f(mid, Lp) <= L)
                {
                    low = mid;
                }
                else
                {
                    hi = mid;
                }
            }
            r = low;
            ans = r - sqrt((r * r) - ((L / 2) * (L / 2)));
        }
        else
        {
            ans = 0;
        }
        printf("%.3lf\n", ans);
        cin >> L >> n >> C;
    }
    return 0;
}