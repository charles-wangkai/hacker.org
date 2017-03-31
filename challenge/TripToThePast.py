#!/usr/bin/env python3

# Q: http://www.hacker.org/challenge/chal.php?id=155
# A: http://www.hacker.org/challenge/chal.php?answer=Remember+Eric+Bina&id=155&go=Submit

import urllib.request

def main():
    req = urllib.request.Request('http://www.hacker.org/challenge/misc/past.php')
    req.add_header('User-Agent', 'NCSA_Mosaic/1.0')
    print(urllib.request.urlopen(req).read().decode())

if __name__ == '__main__':
    main()
