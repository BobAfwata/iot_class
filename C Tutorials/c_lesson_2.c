// single line comment

/* multiple
line
comment
*/

#include <stdio.h>

int main()
{
    int num_1 = 3;
    int num_2 = 2;
    int sum_numbers, diff_numbers, prod_numbers, mod_numbers;
    float quot_numbers;
    
    float x = 4;
    float y = 3;
    
    float z ;
    z = x / y;
    
    
    sum_numbers = num_1 + num_2;
    diff_numbers = num_1 - num_2;
    prod_numbers = num_1 * num_2;
    quot_numbers = num_1 / num_2;
    mod_numbers = num_1 % num_2;
    
    printf("The sum of %d and %d is %d \n", num_1, num_2, sum_numbers);
    printf("The difference of %d and %d is %d \n", num_1, num_2, diff_numbers);
    printf("The product of %d and %d is %d \n", num_1, num_2, prod_numbers);
    printf("The quotient of %d and %d is %.2f \n", num_1, num_2, quot_numbers);
    printf("The modulus of %d and %d is %d \n", num_1, num_2, mod_numbers);
    
    printf("The quotient of %.3f and %.3f is %.3f \n", x, y, z);

    
    
    return 0; 
    
}