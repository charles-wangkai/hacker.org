#!/usr/bin/env python3

# Q: http://www.hacker.org/challenge/chal.php?id=114
# A: http://www.hacker.org/challenge/chal.php?answer=1161269686625383&id=114&go=Submit

def fib(n):
    previous, current = 1, 1
    for _ in range(n - 2):
        previous, current = current, previous + current
    return current

def main():
    print(str(fib(1500000))[::20000])

if __name__ == '__main__':
    main()
