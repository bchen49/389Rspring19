#!/usr/bin/env python3

import hashlib
import string
import socket
import time

def server_crack():
   

    with open(passwords.txt) as passFile
        passwords = passFile.read().splitlines()

    characters = string.ascii_lowercase
    server_ip = '134.209.128.58'
    server_port = 1337

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server_ip, server_port))
    data = s.recv(1024)
    # parse data
    # crack 3 times
    hashes = data.splitlines()

    for i in range(3):
        for c in characters:
            for p in passwords:
                word = hashlib.sha256(c + p)
                if word == hashes[i]:
                    self.s.send(word)
                    sleep.time(5)
                    


if __name__ == "__main__":
    server_crack()