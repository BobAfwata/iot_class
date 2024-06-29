#include <stdio.h>

int main(){
    
    char grade;
    printf("Enter your grade : ");
    scanf("%c", &grade);
    switch(grade){
        case 'A':
            printf("You qualify for Medicine");
            break;
        case 'B':
            printf("You qualify for Engineering");
            break;
        case 'C':
            printf("You qualify for Law");
            break;
        case 'D':
            printf("You qualify for Economics");
            break;
        default:
            printf("You qualify for Arts");
    }
    return 0;
}