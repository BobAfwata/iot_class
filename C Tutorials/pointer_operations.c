#include <stdio.h>

int main(){
    unsigned int x = 20;
    unsigned short y = 15;
    
    double w = 500;
    
    // array of integers
    
    int numbers[5] = {1,2,3,4,5}; 
    
    // integer pointer
    unsigned int *ptr;  // pointer to the integer 
    unsigned short *sptr;
    double *dptr;
    
    int *array_ptr;  // array pointer
    
    array_ptr = &numbers;
    
    ptr = &x;
    sptr = &y;
    dptr = &w;
    
    
    
    printf("0x%X \n" , ptr);
    printf("0x%X \n" , &x);  // address of x 
    
    
    // printf("%d \n" , x);
    // printf("%d \n" , *ptr);  // address of x 
    
    
     printf("0x%X \n" , sptr);
    printf("0x%X \n" , &y);
    
     printf("0x%X \n" , dptr);
    printf("0x%X \n" , &w);
    
     printf("0x%X \n" , sizeof(sptr));
    printf("0x%X \n" , sizeof(dptr));
     printf("0x%X \n" , sizeof(ptr));
    
    return 0;
}