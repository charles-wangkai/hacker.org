#!/usr/bin/env python2.7

# Q: http://www.hacker.org/challenge/chal.php?id=143
# A: http://www.hacker.org/challenge/chal.php?answer=24936&id=143&go=Submit

def main():
    print sum([x * (x - 1) for x in [y * y for y in xrange(3,11)]])

if __name__ == '__main__':
    main()
