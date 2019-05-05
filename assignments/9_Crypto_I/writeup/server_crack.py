#!/usr/bin/env python3

import hashlib
import string
import socket
import time

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

def server_crack():
    hashes = [line.rstrip() for line in open('hashes.txt','r')]
    passwords = [line.rstrip() for line in open('passwords.txt','r')]
    characters = string.ascii_lowercase
    server_ip = '134.209.128.58'
    server_port = 1337

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server_ip, server_port))
    data = s.recv(1024)
    # parse data

    # crack 3 times
    #use crack()

if __name__ == "__main__":
    server_crack()
