#include <stdio.h>

int main()
{
    int iter = 0;
    int x = 20;
    while (iter < 10) {
        printf("Counting %d times \n", iter);
        iter += 1;
    }
    while (x > 0) {
        printf("x = %d \n", x);
        x--;
    }
    return 0;
}
