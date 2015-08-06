#!/usr/bin/env python3

# Q: http://www.hacker.org/challenge/chal.php?id=149
# A: http://www.hacker.org/challenge/chal.php?answer=Nosferatu&id=149&go=Submit

# The boss lies in Level 128. So it will take a long time, would be better to run on a VPS like Amazon EC2.

import DungeonMaster

def main():
    DungeonMaster.play('cavern')

if __name__ == '__main__':
    main()
