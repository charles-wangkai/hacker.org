#!/usr/bin/env python3

# Q: http://www.hacker.org/challenge/chal.php?id=158
# A: http://www.hacker.org/challenge/chal.php?answer=hackadoodle&id=158&go=Submit

import DidacticXORCipher

def main():
    for key in range(256):
        plain = DidacticXORCipher.decrypt_xor_cipher('948881859781c4979186898d90c4c68c85878f85808b8b808881c6c4828b96c4908c8d97c4878c858888818a8381', key)
        
        if 'please' in plain:
            print('key = ' + str(key) + ': ' + plain)

if __name__ == '__main__':
    main()
