#!/usr/bin/env python3

# Q: http://www.hacker.org/challenge/chal.php?id=157
# A: http://www.hacker.org/challenge/chal.php?answer=random+seed&id=157&go=Submit

def decrypt_xor_cipher(cipher, b, x):
    plain = ''
    for byte in bytes.fromhex(cipher):
        plain += chr(byte ^ b)
        b = (b + x) % 256
    return plain

def main():
    print(decrypt_xor_cipher('3d2e212b20226f3c2a2a2b', 79, 0))

if __name__ == '__main__':
    main()
