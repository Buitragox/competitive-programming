/*
# Jhoan Manuel Buitrago Chavez
# 8953846
# 14/04/2022
# dd/mm/yyyy

# Problem link: https://onlinejudge.org/external/111/11127.pdf

# Helps and tips: Carlos Ramirez, Juan Fernando Plata

#Almost same algorithm as python
*/

#include <stdio.h>

int counter = 0;
int changes[] = {'0', '1'};
int N = 0;
char pattern[35];

/* Check if there is a triple SSS in the string pattern[:(i+1)] */
int has_triple(int i)
{
    int triple = 0; /* If True, a triple (SSS) was found */
    int M = i + 1;
    int disp = 1; /* displacement */
    int k, equal;
    
    while ((disp <= (M / 3)) && !(triple)) 
    {
        k = 0;
        equal = 1;
        while ((k < disp) && equal)
        {
            if ((pattern[i - k] != pattern[i - k - disp]) ||
               (pattern[i - k] != pattern[i - k - (disp * 2)]))
                   equal = 0;
            k++;
        }
        if (equal)
            triple = 1;
        
        disp++;
    }
    
    return triple;
}

void count_triple_free(int i)
{
    int is_triple;
    int k, p;
    
    if (i == N)
    {
        counter++;
    }

    else if (pattern[i] == '*')
    {
        for (p = 0; p < 2; p++)
        {
            pattern[i] = changes[p];
            if ((i < 2) || !(has_triple(i)))
            {
                count_triple_free(i + 1);
            }
        }
        pattern[i] = '*';
    }

    else if ((i < 2) || !(has_triple(i)))
    {
        count_triple_free(i + 1);
    }
}

int main()
{
    int i, j;
    char space;
    scanf("%d", &N);
    int cases = 0;
    while (N != 0)
    {
        cases++;
        counter = 0;
        scanf("%c", &space);
        for (j = 0; j < N; j++)
            scanf("%c", &pattern[j]);


        count_triple_free(0);

        printf("Case %d: %d\n", cases, counter);

        scanf("%d", &N);
    }
    return 0;
}
