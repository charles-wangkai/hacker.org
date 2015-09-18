#!/usr/bin/env python3

# Q: http://www.hacker.org/challenge/chal.php?id=50
# A: http://www.hacker.org/challenge/chal.php?answer=babouchka&id=50&go=Submit

# https://en.wikipedia.org/wiki/Matryoshka_doll

import gzip
import urllib.request

def main():
    content = urllib.request.urlopen('http://www.hacker.org/challenge/misc/doll.bin').read()
    
    while True:
        try:
            content = gzip.decompress(content)
        except:
            break
        
    print(content.decode())

if __name__ == '__main__':
    main()
