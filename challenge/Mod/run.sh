#!/bin/bash

# Q: http://www.hacker.org/challenge/chal.php?id=121
# A: http://www.hacker.org/challenge/chal.php?answer=0%3C0%3C1%3C%2F1%3C*-p&id=121&go=Submit

../../hackvm.py --init memory.txt program.txt
cat program.txt