#!/usr/bin/env python3

# Q: http://www.hacker.org/challenge/chal.php?id=38
# A: HTTP GET "http://www.hacker.org/challenge/chal.php?id=38&answer=http%3A%2F%2Fwhitehouse.gov&go=Submit" with the modified Referer "http://whitehouse.gov"

import urllib.request
import hacker_org_util

PROBLEM_ID = '38'

def main():
    url = 'http://whitehouse.gov'
    
    print('get url:', hacker_org_util.build_challenge_url(PROBLEM_ID, url))
    
    request = urllib.request.Request(hacker_org_util.build_challenge_url(PROBLEM_ID, url), headers={'Referer': url})
    print(urllib.request.urlopen(request).read().decode())

if __name__ == '__main__':
    main()
