#!/usr/bin/env python3

# Q: http://www.hacker.org/challenge/chal.php?id=29
# A: http://www.hacker.org/challenge/chal.php?answer=wednesday&id=29&go=Submit

def main():
    message = '01110101 01110011 01100101 00100000 01110111 01100101 01100100 01101110 01100101 01110011 01100100 01100001 01111001 00100000 01100110 01101111 01110010 00100000 01110100 01101000 01100101 00100000 01100001 01101110 01110011 01110111 01100101 01110010'
    print(''.join(map(lambda part: chr(int(part, 2)), message.split())))

if __name__ == '__main__':
    main()
