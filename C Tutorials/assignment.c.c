
#include <stdio.h>

int main()
{
    char country[] = {"Kenya", "Tanzania", "Uganda", "Ethiopia", "Rwanda"}
    printf("Enter the name of the country : ");
    scanf("%s", country);
    
    switch(country[]){
        case "Kenya":
            char city[] = "Nairobi";
            printf("The capital of %s is %s", country, city);
        case "Tanzania":
            char city[] = "Dodoma";
            printf("The capital of %s is %s", country, city);
        case "Uganda":
            char city[] = "Kampala";
            printf("The capital of %s is %s", country, city);
        case "Ethiopia":
            char city[] = "Addis Ababa";
            printf("The capital of %s is %s", country, city);
        case "Rwanda":
            char city[] = "Kigali";
            printf("The capital of %s is %s", country, city);
        default:
            printf("Invalid country");
    }
    
    return 0;
}
