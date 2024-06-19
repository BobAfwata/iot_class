
#include <stdio.h>
static int x = 20;
int main (){
// x is a global variabl
  func();
  printf("\n");
  func2();

  return 0;
}
void func(){
	// int x;			// x is an extern variable
	x = x + 2;
	printf ("%d", x);			// prints 20
}
  
void func2(){
    //int x;				// x is an extern variable
	x = x + 8;
	printf ("%d", x);			// prints 20
}