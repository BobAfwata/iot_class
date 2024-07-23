#include <stdio.h>

int main()
{
    int numbers[3][2] = {{2, 1},
                         {4, 6},
                         {3, 5}};
    /*
    printf("%d \n", numbers[0][0]);
    printf("%d \n", numbers[0][1]);
    printf("%d \n", numbers[1][0]);
    printf("%d \n", numbers[1][1]);
    printf("%d \n", numbers[2][0]);
    printf("%d \n", numbers[2][1]);
    */
    numbers[0][0] = 67;
    
    int i;
    int j;
    
    for(i = 0; i < 3; i++){
        for(j = 0; j < 2; j++){
            printf("%d \n", numbers[i][j]);
        }
    }
    return 0;
}