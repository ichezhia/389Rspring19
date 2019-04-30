#!/usr/bin/env python3

import hashlib
import string

def crack():

    hashes = [line.rstrip() for line in open('hashes.txt','r')]
    passwords = [line.rstrip() for line in open('passwords.txt','r')]
    characters = string.ascii_lowercase

    for c in characters:
        for p in passwords:
            brute_string = c+p
            hash = hashlib.sha256(brute_string).hexdigest()

#check all hashes
            if hash in hashes:
                    print("FOUND! character: " + c + " password: " + p + " is hash: " + hash)


if __name__ == "__main__":
    crack()
