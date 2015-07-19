#!/usr/bin/env python3

# Q: http://www.hacker.org/challenge/chal.php?id=61
# A: http://www.hacker.org/challenge/chal.php?answer=532005663005364261216414503026065341004024261231&id=61&go=Submit

def to_base(number, base):
    result = ''
    while number:
        result = str(number % base) + result
        number //= base
    return result

def main():
    print(to_base(28679718602997181072337614380936720482949, 7))

if __name__ == '__main__':
    main()
