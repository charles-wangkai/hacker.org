#!/usr/bin/env python3

# Q: http://www.hacker.org/challenge/chal.php?id=77
# A: (Not fixed answer, so run this script)

import re
import TypeFast

PROBLEM_ID = '78'

def main():
    TypeFast.solve(PROBLEM_ID, 'Please type the paragraph you see below quickly', lambda s: re.sub(r'<span style="font-size:8%">FOO</span>', '', s))

if __name__ == '__main__':
    main()
