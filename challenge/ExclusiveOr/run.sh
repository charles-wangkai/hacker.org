#!/bin/bash

# Q: http://www.hacker.org/challenge/chal.php?id=125
# A: http://www.hacker.org/challenge/chal.php?answer=13%3E+0%3C1%3C+%3A88*%3F+0%3C0%3C2%2F0%5E0%3E2*-+1%3C1%3C2%2F0%5E1%3E2*-+%3A6%3F+1+2g+0+3%3C*2%3C%2B2%3E+3%3C2*3%3E+089*-g++2%3Cp&id=125&go=Submit

../../hackvm.py --init memory.txt program.txt
cat program.txt