/* 
    Made by Jhoan Buitrago 05/12/2021
                           dd/mm/aaaa

    Problem: https://onlinejudge.org/external/101/10189.pdf
*/

#include <stdio.h>
#include <stdlib.h>
#define MAXCOL 105

char board[105][MAXCOL];
int rows;
int cols;

/* clock wise, start from left, end at bottom left */
int rowChange[] = {0, -1, -1, -1, 0, 1, 1, 1};
int colChange[] = {-1, -1, 0, 1, 1, 1, 0, -1};

/* Trying new curly brackets and parenthesis style O.O */

void countMines() {
    int mines;
    int r, c;
    int i, j, k; /* Cannot initialize variables inside for loops on 98 :C */
    for(i = 0; i < rows; i++) {
        for(j = 0; j < cols; j++) {
            mines = 0;
            if (board[i][j] != '*') { /* If it's not a mine */
                
                for(k = 0; k < 8; k++) { 
                    r = i + rowChange[k];
                    c = j + colChange[k];
                    if (r >= 0 && r < rows && c >= 0 && c < cols) /* If inside the board*/
                        mines = (board[r][c] == '*') ? mines + 1 : mines; /* If a mine ++ */
                }
                board[i][j] = (char) (mines + 48); /* digit + 48 = ascii digit */
            }
        }
    }
}

void printBoard() {
    int i;
    for(i = 0; i < rows; i++) {
        board[i][cols] = '\0';
        printf("%s\n", board[i]);
    }
}


int main() {
    int i;
    int cases = 1;
    scanf("%d%d\n", &rows, &cols);
    while (rows != 0 && cols != 0) {
        
        for(i = 0; i < rows; i++) {
            fgets(board[i], MAXCOL - 1, stdin); /* Apparently fgets is good idk */
        }

        countMines();
        printf("Field #%d:\n", cases++);
        printBoard();

        scanf("%d%d\n", &rows, &cols);
        if (rows != 0 && cols != 0)
            printf("\n");
    }
    return 0;
}