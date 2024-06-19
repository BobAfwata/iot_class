
#include <stdio.h>

int main (){
    int age;
    printf("Enter your age : ");
    scanf("%d", &age);
    if (age < 18) {
        printf("You are not allowed to drive \n");
        printf("You are are too young");
    }
    else{ 
        printf("You are allowed to drive");
    }
    return 0;
}