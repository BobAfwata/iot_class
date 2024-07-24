#include <stdio.h>

const float pi = 3.142;

struct Circle{
    float radius, circumference, area;
};

struct Circle get_circle_data();


int main(){
    struct Circle my_circle = get_circle_data();
    
    printf("Radius = %.2f \n Area = %.2f \n Circumference = %.2f \n", 
                my_circle.radius, my_circle.area, my_circle.circumference);
    
    return 0;
}


struct Circle get_circle_data(){
    struct Circle c;
    printf("Enter radius: ");
    scanf("%f", &c.radius);
    
    c.circumference = 2 * pi * c.radius;
    c.area = pi * c.radius * c.radius;
    
    return c;
}