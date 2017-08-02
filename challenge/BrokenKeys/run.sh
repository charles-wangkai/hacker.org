#!/bin/bash

# Q: http://www.hacker.org/challenge/chal.php?id=212
# A: http://www.hacker.org/challenge/chal.php?answer=0%3C0%3C1%3C-00%3C1%3C-2%2F2%2F2%2F2%2F2%2F2%2F2%2F2%2F2%2F2%2F2%2F2%2F2%2F2%2F2%2F2%2F2%2F2%2F2%2F2%2F2%2F2%2F2%2F2%2F2%2F2%2F2%2F2%2F2%2F2%2F2%2F-*-p&id=212&go=Submit

../../hackvm.py --init memory.txt program.txt
cat program.txt