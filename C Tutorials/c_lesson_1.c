// single line comment

/* multiple
line
comment
*/

#include <stdio.h>

int main()
{
    /*
    printf("My name is Gabriel");
    printf("\n");
    printf("I am 17 years old \n");
    printf("PHY \t CHEM \t MATH \t HIST \t BIO \n");
    printf("80 \t 76 \t 92 \t 87 \t 76");
    */
    
    
    // data types
    
    // integers
    int age = 24;
    printf("I am %d years old \n", age);
    float height = 1.7492;
    printf("I am %.2f metres tall \n", height);
    
    // characters
    char grade = 'A';
    printf("My grade is %c \n", grade);
    
    // string
    char name_0[] = "Gabriel";
    printf("My name is %s \n", name_0);
    return 0; 
    
}