#!/usr/bin/env python3

# Q: http://www.hacker.org/challenge/chal.php?id=157
# A: http://www.hacker.org/challenge/chal.php?answer=random+seed&id=157&go=Submit

def main():
    print(''.join(map(lambda byte: chr(byte ^ 79), bytes.fromhex('3d2e212b20226f3c2a2a2b'))))

if __name__ == '__main__':
    main()
