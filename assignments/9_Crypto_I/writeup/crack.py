#!/usr/bin/env python3

import hashlib
import string

def crack():
    with open(hashes.txt) as hashFile:
    	hashes = hashFile.read().splitlines()

    with open(passwords.txt) as passFile
    	passwords = passFile.read().splitlines()

    characters = string.ascii_lowercase

    for c in characters:
        for p in passwords:
            
            word = hashlib.sha256(c + p)

            for h in hashes:
            	if word == h:
            		print p + ":" + word

            # print hashes as 'input:hash'
            # i.e.  yeet:909104cdb5b06af2606ed4a197b07d09d5ef9a4aad97780c2fe48053bce2be52

if __name__ == "__main__":
    crack()
