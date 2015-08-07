#!/bin/bash

# Q: http://www.hacker.org/challenge/chal.php?id=14
# A: http://www.hacker.org/challenge/chal.php?answer=maniocmaniac&id=14&go=Submit

curl -s http://www.hacker.org/challenge/img/boxes.gif | strings | tail -n 1