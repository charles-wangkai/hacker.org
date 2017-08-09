#!/bin/bash

# Q: http://www.hacker.org/challenge/chal.php?id=216
# A: Due to the URL length limitation, submit the answer by HTTP POST.
# URL: http://www.hacker.org/challenge/chal.php?id=216&go=Submit
# Content-Type: application/x-www-form-urlencoded
# Data: answer=<content in the file program.txt>

../../hackvm.py --init memory.txt program.txt
cat program.txt