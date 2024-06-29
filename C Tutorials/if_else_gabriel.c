#include <stdio.h>

int main(){
    int salary;
    printf("Enter your monthly salary : ");
    scanf("%d", &salary);
    printf("Old salary : %d \n", salary);
    if (salary < 50000){
        salary *= 1.1;
        
    }
    else if (salary >= 50000 && salary < 80000){
        salary /= 0.95;
        
    }
    else {
        salary = salary * 0.95;
        
    }
    printf("New salary : %d \n", salary);
    return 0;
}