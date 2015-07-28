#!/usr/bin/env python3

# Q: http://www.hacker.org/challenge/chal.php?id=198
# A: (My current IP address. Not fixed answer, so run this script)

import urllib.request
import webbrowser
from challenge import hacker_org_util

PROBLEM_ID = '198'

def main():
    answer = urllib.request.urlopen('http://bot.whatismyipaddress.com/').read().decode()
    print(answer)
    
    webbrowser.open(hacker_org_util.build_challenge_url(PROBLEM_ID, answer))

if __name__ == '__main__':
    main()
