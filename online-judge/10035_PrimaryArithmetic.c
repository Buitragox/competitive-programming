#include <stdio.h>
/*
// Made by Jhoan Buitrago 07/10/2021 dd/mm/aaaa

// Problem https://onlinejudge.org/external/100/10035.pdf
*/
int main()
{
    int x, y, carry, dX, dY, count;

    scanf("%d%d", &x, &y);
    while(x != 0 || y != 0)
    {
        carry = 0;
        count = 0;
        if(y > x)
        {
            int tmp = y;
            y = x;
            x = tmp;
        }
        while(x > 0)
        {
            dX = x % 10; /*Get last digit*/
            dY = y % 10;
            if(dX + dY + carry >= 10)
            {
                count++;
                carry = 1;
            }
            else
            {
                carry = 0;
            }
            x /= 10; /*Delete last digit*/
            y /= 10;
        }

        if(count == 0)
            printf("No carry operation.\n");
        else if(count == 1)
            printf("1 carry operation.\n");
        else
            printf("%d carry operations.\n", count);

        scanf("%d%d", &x, &y);
    }
}