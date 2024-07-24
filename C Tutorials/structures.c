#include <stdio.h>

struct Student
{
  char name[32];
  int age;
  float height;
};

typedef struct Student Student;


struct Rectangle
{
  float length;
  float width;
  float area;
};

//struct Rectangle my_rectangle;

float calculate_area(struct Rectangle);

int main ()
{
  Student student_1 = { "Gabriel Opiyo", 17, 1.85 };
  Student student_2 = { "Martin Wasike", 17, 1.83 };
  Student student_3 = { "Henry Okii", 18, 1.76 };

  struct Rectangle screen;
  screen.length = 160;			//cn 
  screen.width = 200;
  screen.area = calculate_area(screen);
  
  
  printf ("Length = %.2f \n Width = %.2f \n Area = %.2f \n", screen.length,
		  screen.width, screen.area);



  printf ("The first student is called %s \n", student_1.name);
  printf ("The age of the first student is %d \n", student_1.age);
  printf ("The height of the first student is %.2f m \n", student_1.height);
  return 0;
}


float calculate_area(struct Rectangle my_rectangle){
    
   // struct Rectangle my_rectangle;
    
    my_rectangle.area = my_rectangle.length * my_rectangle.width;
    
    return my_rectangle.area;
    
}