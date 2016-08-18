#!/usr/bin/env python3

# Q: http://www.hacker.org/challenge/chal.php?id=27
# A: HTTP POST to "http://www.hacker.org/challenge/chal.php?answer=marmelade&id=27&go=Submit" with empty data

import urllib.request
import hacker_org_util

PROBLEM_ID = '27'

def main():
    print(urllib.request.urlopen(hacker_org_util.build_challenge_url(PROBLEM_ID, 'marmelade'), data=b'').read().decode())

if __name__ == '__main__':
    main()
