#!/usr/bin/env python3

# Q: http://www.hacker.org/challenge/chal.php?id=159
# A: http://www.hacker.org/challenge/chal.php?answer=fiendster&id=159&go=Submit

import string
import DidacticXORCipher

def main():
    cipher = '31cf55aa0c91fb6fcb33f34793fe00c72ebc4c88fd57dc6ba71e71b759d83588'
    for b in range(256):
        for x in range(256):
            plain = DidacticXORCipher.decrypt_xor_cipher(cipher, b, x)
            
            if all(map(lambda c: c in string.printable, plain)):
                print('b = ' + str(b) + ', x = ' + str(x) + ': ' + plain)

if __name__ == '__main__':
    main()
