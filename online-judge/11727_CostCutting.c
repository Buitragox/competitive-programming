#include <stdio.h>
#define MAX_EMPLOYEES 3

int main()
{
    int n, count = 1, diff = 0, minDiff, sum = 0, avg, ans;
   //int employee1, employee2, employee3;
    int employees[MAX_EMPLOYEES];
    scanf("%d", &n);
    while(n--)
    {
        sum = 0;
        for(int i = 0; i < MAX_EMPLOYEES; i++)
        {
            scanf("%d", &employees[i]);
            sum += employees[i];
        }
        
        avg = sum / MAX_EMPLOYEES;
        //printf("%d", avg);

        for(int i = 0; i < MAX_EMPLOYEES; i++)
        {
            diff = avg - employees[i];
            if(diff < 0)
            {
                diff *= -1;
            }
            if(diff < minDiff || i == 0)
            {
                ans = employees[i];
                minDiff = diff;
            }

        }
        printf("Case %d: %d\n", count++, ans);
    }

    return 0;
}