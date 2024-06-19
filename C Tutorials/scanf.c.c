
#include <stdio.h>

int main()
{
    char gender;
    int weight;
    float distance;
    printf("Enter your gender : \n");
    scanf("%c",&gender);
    printf("Your gender is %c \n", gender);
    
    printf("Enter your weight : \n");
    scanf("%d",&weight);
    printf("Your weight is %d kg \n", weight);
    
    printf("Enter distance covered : \n");
    scanf("%f",&distance);
    printf("Your covered %.2f km \n", distance);
    
    

    return 0;
}