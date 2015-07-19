#!/usr/bin/env python3

# Q: http://www.hacker.org/challenge/chal.php?id=59
# A: http://www.hacker.org/challenge/chal.php?answer=extension&id=59&go=Submit

import collections
import urllib.request

def main():
    document = urllib.request.urlopen('http://www.rfc-editor.org/rfc/rfc3280.txt').read().decode()
    print(collections.Counter(filter(lambda word: len(word) == 9, document.split())).most_common(1)[0][0])

if __name__ == '__main__':
    main()
