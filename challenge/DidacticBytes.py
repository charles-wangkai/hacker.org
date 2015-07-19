#!/usr/bin/env python3

# Q: http://www.hacker.org/challenge/chal.php?id=106
# A: http://www.hacker.org/challenge/chal.php?answer=13061578&id=106&go=Submit

def main():
    print(int(''.join(map(lambda number: hex(number)[2:], [199, 77, 202])), 16))

if __name__ == '__main__':
    main()
