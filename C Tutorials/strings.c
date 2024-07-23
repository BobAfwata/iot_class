#include <stdio.h>
#include <string.h>


int main()
{
    char name1[20] = "Gabriel ";
    char name2[20] = "Opiyo"; 
    
    char my_name[20];
    int result;
    result = strcmp(name1, name2);
    if(result == 0){
        printf("The strings are the same \n");
    }
    else {
        printf("The strings are not the same \n");
        printf("%d \n", result);
    }
    strcpy(my_name, name1);
    strcat(name1, name2);
    printf("%s \n", name1);
    
    printf("%s \n", strrev(name1));
    printf("%s \n", strupr(name1));
    printf("%s \n", strlwr(name1));    
    printf("The size of my name is %zu \n", strlen(my_name));
    
    /*
    printf("%s\n", name1);
    printf("%s\n", name2);
    
    printf("%c\n", name1[7]);
    printf("%c\n", name2[7]);
    
   
    
    int i;
    
    for(i = 0; i < strlen(my_name); i++){
        printf("%c \n", my_name[i]);
    }

    puts(my_name);
    */
    return 0;

}