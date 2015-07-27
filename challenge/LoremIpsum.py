#!/usr/bin/env python3

# Q: http://www.hacker.org/challenge/chal.php?id=58
# A: http://www.hacker.org/challenge/chal.php?answer=scatterbrained&id=58&go=Submit

import collections
import re
import urllib.request

def main():
    text = urllib.request.urlopen('http://www.hacker.org/challenge/misc/lorem.txt').read().decode()
    print(list(filter(lambda element: element[1] == 1, collections.Counter(re.findall(r'\w+', text)).most_common()))[0][0])

if __name__ == '__main__':
    main()
