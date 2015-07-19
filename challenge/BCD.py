#!/usr/bin/env python3

# Q: http://www.hacker.org/challenge/chal.php?id=39
# A: http://www.hacker.org/challenge/chal.php?answer=739391&id=39&go=Submit

def main():
    message = '0111 0011 1001 0011 1001 0001'
    print(*map(lambda part: int(part, 2), message.split()), sep='')

if __name__ == '__main__':
    main()
