#!/usr/bin/env python3

# Q: http://www.hacker.org/challenge/chal.php?id=156
# A: http://www.hacker.org/challenge/chal.php?answer=X&id=156&go=Submit

def main():
    print(chr(int('9f', base=16) ^ int('c7', base=16)))

if __name__ == '__main__':
    main()
