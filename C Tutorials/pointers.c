
#include <stdio.h>

int main()
{
    int number[3] = {10,20,30};
    
    int *ptr ;
    ptr = &number;
    
    printf("first number : %d  \n", number[0]);  // base address 
    printf("first number : %d  \n", *ptr);
    printf("size of ptr  : %d  \n", sizeof(ptr));

    
    
    printf("second number : %d  \n", number[1]);
    printf("second number : %d  \n", *ptr + 1); // 10 +1 = 11
    printf("second number : %d  \n", *(ptr + 1)); //20  (ptr + 1 )  -> 4 bytes 
    ptr++;
    ptr++;
    printf("third number : %d  \n", *ptr); //20  (ptr + 1 )  -> 4 bytes 



    
    return 0;
}
