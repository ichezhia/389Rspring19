# Writeup 7 - Binaries I

Name: Iniyan Chezhian
Section: 0101

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: Iniyan Chezhian

## Assignment Writeup

### Part 1 (90 Pts)

I started off by noticing the 0x in front of something that looked liked hex. This tells me that this is probably a number or something. I assumed it was an int. There are two of these. Then I see that there are some prints, so I added these to my C file. Then I see the xor, which is ^=. Then I see that there is a data section which provides the formatting for the print I already found, so I adjusted the formatting of my print statements accordingly. I see the idea that before every print or xor, I can see what is the mov before it and this tells me what variable was used. I was unable to determine the variabled names for the variables, so I just used foo1 and foo2; I could have assumed that foo1 was b and foo2 was a, but not not make that assumption. I then used gdb to polish the rest of the code and acheive the C code below. Running my code through gdb was helpful to fix the formatting and other minor details I was missing, such as the #include stdio.h, int main(), etc. Finally, I did gccx and have the a.out file in this folder as well and the output below the code below.

```c
printf("your code here");
```

```

```

### Part 2 (10 Pts)

Two variables are defined. Then they are printed. Then exponential operations are performed in various ways on the variables. Then they are printed again. The output is above. These instructions achieve mathematical exponential operations on integers.
