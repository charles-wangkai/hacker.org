#!/bin/bash

# Q: http://www.hacker.org/challenge/chal.php?id=209
# A: http://www.hacker.org/challenge/chal.php?answer=0+0%5E1%2B+1%5E%3C+1%5E%3C+%3A56*%3F+1%2B+0%5E34*%3A1%2B048*-%3F+d1%2B+068*-g+1%5E%3Cp&id=209&go=Submit

../../hackvm.py --init memory.txt program.txt
cat program.txt