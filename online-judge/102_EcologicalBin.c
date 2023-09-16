// Made by Jhoan Buitrago 03/10/2021 dd/mm/aaaa

// Problem https://onlinejudge.org/external/1/102.pdf

// Solved with brute force

#include <stdio.h>

int main()
{
    int arr[3][3];
    //All possible combinations in alphabetical order
    int combs[6][3] = {{0,2,1}, {0, 1, 2}, {2, 0, 1}, {2, 1, 0}, {1, 0, 2}, {1, 2, 0}};
    char bins[6][5] = {"BCG", "BGC", "CBG", "CGB", "GBC", "GCB"}; 
    while(scanf("%d", &arr[0][0]) == 1)
    {
        for(int i = 0; i < 3; i++)
        {
            for(int j = 0; j < 3; j++)
                if(!(i == 0 && j == 0)) //Ignore first one since its already been read.
                {
                    scanf("%d", &arr[i][j]);
                }
        }
        int mov, minMov = 0, ind;
        for(int k = 0; k < 6; k++)
        {
            mov = 0;
            for(int i = 0; i < 3; i++)
            {
                for(int j = 0; j < 3; j++)
                {
                    if(j != combs[k][i]) // Ignoring value of the color that is assign to the bin 
                                         // in this combination
                    {
                        mov += arr[i][j];
                    }
                }
            }
            if(mov < minMov | k == 0)
            {
                minMov = mov;
                ind = k; // Remember index of solution to print it later.
            }
        }
        printf("%s %d\n", bins[ind], minMov);
    }
    return 0;
}