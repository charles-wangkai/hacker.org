#!/usr/bin/env python3

# Q: http://www.hacker.org/challenge/chal.php?id=166
# A: http://www.hacker.org/challenge/chal.php?answer=penguinicity&id=166&go=Submit

import itertools
import string

ALPHABET = string.ascii_letters + ' ,.`'

def decrypt_part(cipher, first):
    s = bytes.fromhex(cipher)
    
    for x_byte in range(0x100):
        for key_byte in range(0x100):
            valid = True
            current_key_byte = key_byte
            for i in range(len(s)):
                c = current_key_byte ^ s[i]
                
                if (i == 0 and chr(c) != first) or (i != 0 and all(map(lambda offset: c + offset >= 0 and chr(c + offset) not in ALPHABET, range(-1, 2)))):
                    valid = False
                    break
                
                current_key_byte = (s[i] + x_byte) % 0x100
            
            if valid:
                return x_byte, key_byte

def decrypt_feedback_cipher_long(cipher, key, x):
    s = bytes.fromhex(cipher)
    
    plain = ''
    for i in range(0, len(s), 4):
        s_part = s[i:i + 4]
        part = int.from_bytes(s_part, byteorder='little')
        c = key ^ part
        
        decrypted = ''.join(map(chr, c.to_bytes(4, byteorder='little')))[:len(s_part)]
        for ch in decrypted:
            if ch not in ALPHABET:
                return None
        
        plain += decrypted

        key = (part + x) % 0x100000000
    return plain

def main():
    cipher = '5499fa991ee7d8da5df0b78b1cb0c18c10f09fc54bb7fdae7fcb95ace494fbae8f5d90a3c766fdd7b7399eccbf4af592f35c9dc2272be2a45e788697520febd8468c808c2e550ac92b4d28b74c16678933df0bec67a967780ffa0ce344cd2a9a2dc208dc35c26a9d658b0fd70d00648246c90cf828d72a794ea94be51bbc6995478505d37b1a6b8daf7408dbef7d7f9f76471cc6ef1076b46c911aa7e75a7ed389630c8df32b7fcb697c1e89091c30be736a4cbfe27339bb9a2a52a280'
    
    x_bytes = []
    key_bytes = []
    plain_head = 'I ha'
    for i in range(4):
        x_byte, key_byte = decrypt_part(''.join([cipher[j:j + 2] for j in range(i * 2, len(cipher), 8)]), plain_head[i])
        
        x_bytes.append(x_byte)
        key_bytes.append(key_byte)
    
    key = int.from_bytes(bytes(key_bytes), byteorder='little')
    
    for x_byte_offsets in itertools.product(range(-1, 1), repeat=4):
        x = int.from_bytes(bytes(map(lambda i: x_bytes[i] + x_byte_offsets[i], range(4))), byteorder='little')
        
        plain = decrypt_feedback_cipher_long(cipher, key, x)
        if plain:
            print('key = ' + str(key) + ', x = ' + str(x) + ': ' + plain)
    
if __name__ == '__main__':
    main()
