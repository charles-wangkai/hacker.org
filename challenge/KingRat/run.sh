#!/bin/bash

# Q: http://www.hacker.org/challenge/chal.php?id=129
# A: http://www.hacker.org/challenge/chal.php?answer=36*1%2B%3C36*1%2B+0%5E59*%3F+1-0%5E%3C2%5E1%5E%3A+45*%3F+2%5E1%5E%3A1-+9%3F+2vd1v2g+d077*-g++dp%21&id=129&go=Submit

../../hackvm.py --init memory.txt program.txt
cat program.txt