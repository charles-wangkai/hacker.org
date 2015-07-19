#!/usr/bin/env python3

# Q: http://www.hacker.org/challenge/chal.php?id=115
# A: http://www.hacker.org/challenge/chal.php?answer=2277532&id=115&go=Submit

def is_square(number):
    return round(number ** 0.5) ** 2 == number

def main():
    LIMIT = 2118
    print(sum(map(lambda number: number * 2 if is_square(number) else number, range(LIMIT + 1))))

if __name__ == '__main__':
    main()
