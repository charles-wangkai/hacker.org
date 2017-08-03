#!/usr/bin/env python3

# Q: http://www.hacker.org/challenge/chal.php?id=165
# A: http://www.hacker.org/challenge/chal.php?answer=kettlewon&id=165&go=Submit

def decrypt_feedback_cipher_long(cipher, key):
    s = bytes.fromhex(cipher)
    
    plain = ''
    for i in range(0, len(s), 4):
        part = int.from_bytes(s[i:i + 4], byteorder='big')
        c = key ^ part
        plain += ''.join(map(chr, c.to_bytes(4, byteorder='big')))
        key = part
    return plain

def main():
    key = 0
    
    plain = decrypt_feedback_cipher_long('e5534adac53023aaad55518ac42671f8a1471d94d8676ce1b11309c1c27a64b1ae1f4a91c73f2bfce74c5e8e826c27e1f74c4f8081296ff3ee4519968a6570e2aa0709c2c4687eece44a1589903e79ece75117cec73864eebe57119c9e367fefe9530dc1', key)
    
    print('key = ' + str(key) + ': ' + plain)

if __name__ == '__main__':
    main()
