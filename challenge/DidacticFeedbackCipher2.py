#!/usr/bin/env python3

# Q: http://www.hacker.org/challenge/chal.php?id=163
# A: http://www.hacker.org/challenge/chal.php?answer=cornishpasty&id=163&go=Submit

def decrypt_feedback_cipher(cipher, key, x):
    s = bytes.fromhex(cipher)
    
    plain = ''
    for i in range(len(s)):
        c = key ^ s[i]
        plain += chr(c)
        key = (s[i] + x) % 0x100
    return plain

def main():
    for x in range(256):
        for key in range(256):
            plain = decrypt_feedback_cipher('310a7718781f734c31425e775a314f3b40132c5122720599b2dfb790fd8ff894add2a4bdc5d1a6e987a0ed8eee94adcfbb94ee88f382127819623a404d3f', key, x)
            
            if 'I think' in plain:
                print('key = ' + str(key) + ', x = ' + str(x) + ': ' + plain)

if __name__ == '__main__':
    main()
