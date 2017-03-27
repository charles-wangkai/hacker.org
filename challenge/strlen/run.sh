#!/bin/bash

# Q: http://www.hacker.org/challenge/chal.php?id=66
# A: http://www.hacker.org/challenge/chal.php?answer=0+0%5E%3C+9%3F+1%2B09-6-g+p%21&id=66&go=Submit

../../hackvm.py --init memory.txt program.txt
cat program.txt