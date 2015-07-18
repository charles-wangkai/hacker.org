#!/usr/bin/env python3

# Q: http://www.hacker.org/challenge/chal.php?id=76
# A: (Not fixed answer, so run this script)

import re
import urllib.request
from challenge import hacker_org_util

PROBLEM_ID = '76'

def main():
    source = urllib.request.urlopen(hacker_org_util.build_challenge_url(PROBLEM_ID)).read().decode()
    
    answer = re.search(r'Please type the sentence you see below quickly.*<b>(.*)</b>', source, flags=re.DOTALL).group(1).strip()
    print(answer)
    
    print(urllib.request.urlopen(hacker_org_util.build_challenge_url(PROBLEM_ID, answer)).read().decode())

if __name__ == '__main__':
    main()
