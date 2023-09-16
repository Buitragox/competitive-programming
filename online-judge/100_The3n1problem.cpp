#include <iostream>

using namespace std;

int threeNPlus1(int numb)
{
    int count = 1;
    while(numb != 1)
    {
        //cout << numb << endl;
        count++;
        if(numb % 2 != 0)
        {
            numb = 3 * numb + 1; 
        }
        else
        {
            numb = numb / 2;
        }
    }
    //cout << numb << endl;
    return count;
}

int main()
{
    int left, right, maxN = 0, temp;
    int auxLeft, auxRight;
    while(cin >> left >> right)
    {
        auxLeft = left;
        auxRight = right;
        if(left > right)
        {
            auxLeft = right;
            auxRight = left; 
        }
        maxN = 0;
        for(int i = auxLeft; i <= auxRight; i++)
        {
            temp = threeNPlus1(i);
            if(temp > maxN)
            {
                maxN = temp;
            }
        }
        cout << left << " " << right << " " << maxN << "\n";
    }
    return 0;
}