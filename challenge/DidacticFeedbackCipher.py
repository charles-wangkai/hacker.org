#!/usr/bin/env python3

# Q: http://www.hacker.org/challenge/chal.php?id=162
# A: http://www.hacker.org/challenge/chal.php?answer=ottomelon&id=162&go=Submit

def decrypt_feedback_cipher(cipher, key):
    s = bytes.fromhex(cipher)
    
    plain = ''
    for i in range(len(s)):
        c = key ^ s[i]
        plain += chr(c)
        key = s[i]
    return plain

def main():
    for key in range(256):
        plain = decrypt_feedback_cipher('751a6f1d3d5c3241365321016c05620a7e5e34413246660461412e5a2e412c49254a24', key)
        
        if 'Your' in plain:
            print('key = ' + str(key) + ': ' + plain)

if __name__ == '__main__':
    main()
