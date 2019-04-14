/*
 * Name: Iniyan Chezhian
 * Section: 0101
 *
 * I pledge on my honor that I have not given or received any unauthorized
 * assistance on this assignment or examination.
 *
 * Digital acknowledgement: Iniyan Chezhian
 */

#include <stdio.h>

 int main()
 {
   int foo1 = 485163226;
   int foo2 = 4277009102;

   printf("a = %d\n", foo2);
   printf("b = %d\n", foo1);

   foo2^=foo1;
   foo1^=foo2;
   foo2^=foo1;

   printf("a = %d\n", foo2);
   printf("b = %d\n", foo1);

   return 0;
}
