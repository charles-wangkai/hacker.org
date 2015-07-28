#!/usr/bin/env python3

# Q: http://www.hacker.org/challenge/chal.php?id=198
# A: (My current IP address. Not fixed answer, so run this script)

import urllib.request

def main():
    answer = urllib.request.urlopen('http://bot.whatismyipaddress.com/').read().decode()
    print(answer)

if __name__ == '__main__':
    main()
