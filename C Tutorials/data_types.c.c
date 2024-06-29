
#include <stdio.h>

int main()
{
    char grade ='c';
    int age = 24;
    float height = 176.283;
    double number = 112.345678;
    printf("characters : %u bytes ", sizeof(grade) );
    // unsigned
    printf("\n");
    printf("integer : %u  bytes ", sizeof(age));
    printf("\n");
    printf("float : %u bytes ", sizeof(height));
    printf("\n");
    printf("double : %u bytes ", sizeof(number));
    printf("\n");
    
    

    return 0;
}