/* 
    Made by Jhoan Buitrago 10/12/2021
                           dd/mm/aaaa

    Problem: https://onlinejudge.org/external/101/10189.pdf
*/

#include <stdio.h>

int arr[55];

void swap(int i, int j)
{
    int tmp = arr[i];
    arr[i] = arr[j];
    arr[j] = tmp;
}

int simpleSort(int arrlen)
{
    int swaps = 0;
    int ifSwaped = 1;
    int i;
    int j = 0;
    /* If i could swap something last iteration 
       then I can still try to sort */
    while(ifSwaped) 
    {
        ifSwaped = 0;
        for(i = 1; i < arrlen - j; i++)
        {
            if(arr[i] < arr[i - 1])
            {
                swap(i, i - 1);
                ifSwaped = 1;
                swaps++;
            }
        }
        j++;
    }

    return swaps;
}


int main() 
{
    int cases, arrlen;
    int i, ans;
    scanf("%d", &cases);
    while(cases--)
    {
        scanf("%d", &arrlen);   
        for(i = 0; i < arrlen; i++)
        {
            scanf("%d", &arr[i]);
        }
        
        ans = 0;

        if(arrlen > 0)
            ans = simpleSort(arrlen);

        printf("Optimal train swapping takes %d swaps.\n", ans);
    }
    
    return 0;
}