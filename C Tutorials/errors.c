#include <stdio.h>
#include "number.h"
int number = 10;
extern int mynumber;
int main(){
    printf("%d", number);
    printf("\n");
    printf("%d", mynumber);
   
    return 0;
}