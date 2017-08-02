#!/bin/bash

# Q: http://www.hacker.org/challenge/chal.php?id=211
# A: http://www.hacker.org/challenge/chal.php?answer=0%3C1%3C-58*%3F+0%3C1%3C+1%5E2%2F1%5E2%2F-44*%3F+1v2%2F1v2%2F047*-g+-1%2B6%3F+0%3Cp%21+1%3Cp%21&id=211&go=Submit

../../hackvm.py --init memory.txt program.txt
cat program.txt