/* 
# Jhoan Manuel Buitrago Chavez
# 8953846
# 13/04/2022
# dd/mm/yyyy

# Problem link: https://onlinejudge.org/external/117/11753.pdf
*/


#include <stdio.h>

#define MAX_SIZE 10050

int nums[MAX_SIZE];

int min(int a, int b)
{
    return (a < b) ? a : b;
}

int solve(int left, int right, int inserts, int K)
{
    int ans = 0;
    if ((left >= right) || (inserts > K))
        ans = inserts;
    else if (nums[left] == nums[right])
        ans = solve(left + 1, right - 1, inserts, K);
    else
    {
        /* add numbers to the left of nums[left], or the right of nums[right] */
        ans = min(solve(left, right - 1, inserts + 1, K),
                  solve(left + 1, right, inserts + 1, K));
    }
        
    return ans;
}

int main()
{
    int cases, N, K, i, inserts;
    scanf("%d", &cases);
    int c = 1;
    while (c <= cases)
    {
        scanf("%d%d", &N, &K);
        for (i = 0; i < N; i++)
        {
            scanf("%d", &nums[i]);
        } 

        inserts = solve(0, N - 1, 0, K);

        printf("Case %d: ", c++);
        if (inserts > K)
            printf("Too difficult\n");
        else if (inserts == 0)
            printf("Too easy\n");
        else
            printf("%d\n", inserts);

    } 
    return 0;
}