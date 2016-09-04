#!/usr/bin/env python3

# Q: http://www.hacker.org/challenge/chal.php?id=139
# A: http://www.hacker.org/challenge/chal.php?answer=sunshine&id=139&go=Submit

import re
import urllib.request
import hacker_org_util

PROBLEM_ID = '139'

def main():
    source = urllib.request.urlopen(hacker_org_util.build_challenge_url(PROBLEM_ID)).read().decode()
    
    m = re.search('<p>(.*)<p>', source, flags=re.DOTALL)
    text = m.group(1)
    
    print(''.join(re.findall(r'[A-Z]', text)))

if __name__ == '__main__':
    main()
