#!/usr/bin/env python3

# Q: http://www.hacker.org/challenge/chal.php?id=157
# A: http://www.hacker.org/challenge/chal.php?answer=random+seed&id=157&go=Submit

def decrypt_xor_cipher(cipher, key):
    return ''.join(map(lambda byte: chr(byte ^ key), bytes.fromhex(cipher)))

def main():
    print(decrypt_xor_cipher('3d2e212b20226f3c2a2a2b', 79))

if __name__ == '__main__':
    main()
