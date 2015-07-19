#!/usr/bin/env python3

# Q: http://www.hacker.org/challenge/chal.php?id=1
# A: http://www.hacker.org/challenge/chal.php?answer=fishcake&id=1&go=Submit

# https://en.wikipedia.org/wiki/ROT13

import os
import sys

def main():
    cipher = 'Guvf zrffntr vf rapelcgrq va ebg 13. Lbhe nafjre vf svfupnxr.'
    
    actualstdout = sys.stdout
    sys.stdout = open(os.devnull, 'w')
    import this
    sys.stdout = actualstdout
    
    print(''.join([this.d.get(c, c) for c in cipher]))

if __name__ == '__main__':
    main()
