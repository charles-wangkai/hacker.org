#!/usr/bin/env python3

# Q: http://www.hacker.org/challenge/chal.php?id=187
# A: http://www.hacker.org/challenge/chal.php?answer=6307248905694960523281201519065112560315109266120946334276511258112647455670688177420019237462570351&id=187&go=Submit

import urllib.request

def main():
    req = urllib.request.Request('http://www.hacker.org/challenge/misc/toomany/infinite_number.txt')
    req.add_header('Range', 'bytes=999999999999999999999999999999999999999999999999999-1000000000000000000000000000000000000000000000000098')
    print(urllib.request.urlopen(req).read().decode())

if __name__ == '__main__':
    main()
