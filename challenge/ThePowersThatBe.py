#!/usr/bin/env python3

# Q: http://www.hacker.org/challenge/chal.php?id=34
# A: http://www.hacker.org/challenge/chal.php?answer=7496883104146177&id=34&go=Submit

def main():
    print(str((17 ** 39) ** 11)[::33])

if __name__ == '__main__':
    main()
