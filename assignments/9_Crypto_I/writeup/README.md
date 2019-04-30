# Crypto I Writeup

Name: Iniyan Chezhian
Section: 0101

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: Iniyan Chezhian

## Assignment Writeup

### Part 1 (70 Pts)

Here is what my `crack.py` was able to find:

```
FOUND! character: a password: freedom is hash: 52e5a82e5763533be232e82482d3e6f44118f88b1b6bd3224134341979fe43cc
FOUND! character: a password: password is hash: 739145a8634b184276559a2f3055353db3b261109649ef78445149415f0b4dee
FOUND! character: b password: 1234567890 is hash: f3a885dd12d13ad8e58b5f6c10730a720f61103f651dfb0f49670bad8c7305d5
FOUND! character: g password: westside is hash: 518499174f0754eaf5421fdc17499bc8865b4c6419fbf616f17d38eb741073aa
FOUND! character: n password: superman is hash: 7e4096245b7ce7689e665c9054d612c1894ad0d182b60b5a9be1c8b10e817306
FOUND! character: o password: whatever is hash: 833c3b30b541406a644932cd498fb4d85c65f11e4968333be659c31812d2d6be
FOUND! character: q password: nicole is hash: dbec1495345f5a1573a0dd437c207cacc844f74b8a7b030c858f4f660bf9484f
FOUND! character: t password: shadow is hash: 3f6c2527aa5f8eb3ae4bd5b33d772ba819196a95f09ad430c67c3b5b9570711e
FOUND! character: u password: welcome is hash: 3d925228586369644c84ae5da6753faf8109db1f725c60ccb6dffb914797d289
FOUND! character: z password: matrix is hash: 247ead31de7efd5c8fd859630ecb959c4e6240646fcd4d41962f25b1fb33c702
```
(It gives the character, password, and what the hash was.)

#### Thought Process
Coding `crack.py` wasn't too bad. I was able to figure out how to read files in python line by line. I initially did: 
```
    hashes = [line.rstrip('\n') for line in open('hashes.txt')]
```

I forgot the `'r'` parameter for the open() function. Then the rstrip() function was not working with the `'\n'` parameter I gave, so I removed that. Then everything worked fine.

As this is O(n^3), it may be a good idea to store possible hashes then check them all at once in the future for larger datasets.

### Part 2 (30 Pts)
This part was attempted in `server_crack.py`, but not completed.
