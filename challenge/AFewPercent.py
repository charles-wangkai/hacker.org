#!/usr/bin/env python3

# Q: http://www.hacker.org/challenge/chal.php?id=24
# A: http://www.hacker.org/challenge/chal.php?answer=fugly&id=24&go=Submit

import urllib.parse

def main():
    message = '%66%75%67%6C%79'
    print(urllib.parse.unquote(message))

if __name__ == '__main__':
    main()
