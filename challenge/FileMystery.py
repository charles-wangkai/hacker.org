#!/usr/bin/env python3

# Q: http://www.hacker.org/challenge/chal.php?id=18
# A: http://www.hacker.org/challenge/chal.php?answer=whattogivemysister&id=18&go=Submit

import gzip
import urllib.request

def main():
    local_filename = urllib.request.urlretrieve('http://www.hacker.org/challenge/misc/fl.bin')[0]

    f = gzip.open(local_filename)
    print(f.read().decode())

if __name__ == '__main__':
    main()
