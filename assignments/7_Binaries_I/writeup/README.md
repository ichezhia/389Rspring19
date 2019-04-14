# Writeup 7 - Binaries I

Name: Iniyan Chezhian
Section: 0101

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: Iniyan Chezhian

## Assignment Writeup

### Part 1 (90 Pts)

#### My Thought Process

I started off by noticing the `0x` in front of something that looked liked hex. This tells me that this is probably a number or something. I assumed it was an `int`. There are two of these. Then I see that there are some prints, so I added `printf`s to my C file. Then I see the `xor`, which is `^=`. Then I see that there is a `data section` which provides the formatting for the print I already found, so I adjusted the formatting of my `printf` statements accordingly. I see the idea that before every `print` or `xor`, I can see what is the mov before it and this tells me what variable was used. I was unable to determine the variabled names for the variables, so I just used `foo1` and `foo2`; I could have assumed that `foo1` was b and `foo2` was a, but chose to not make that assumption. I then used `gdb` to polish the rest of the code and acheive the C code below. Running my code through `gdb` was helpful to fix the formatting and other minor details I was missing, such as the `#include stdio.h`, `int main()`, etc. Finally, I did `gcc` and have the `a.out` file in this folder as well and the output below the code below.

#### main.c
```c
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
```

#### a.out
```
a = -17958194
b = 485163226
a = 485163226
b = -17958194
```

### Part 2 (10 Pts)

The instructions essentially swaps the variables. It does this by using the ^= operator in C.
