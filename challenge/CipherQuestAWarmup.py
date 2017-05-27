#!/usr/bin/env python3

# Q: http://www.hacker.org/challenge/chal.php?id=275
# A: http://www.hacker.org/challenge/chal.php?answer=today+my+boyfriend+told+m&id=275&go=Submit

# Reference: Substitution cipher solver (http://quipqiup.com/index.php)

def main():
    cipher = 'tulgqBmqBvuqbdhpslBtuclBmpBjpBfuzclstBjgsCBuztBxhtjBmpBvpfgzepBjpBbpctBdpgccqBehfk.BhBxpstBtuBjheBjuzepBgsqxgqBtuBezdodhepBjhmBxhtjBjumpmglpBeuzo.BhBxgckBhsBtuBjheBduumBuscqBtuBbhslBjhmBjuukhsCBzoBxhtjBmqBehetpd.BejpBfgstBldhap.BuzdBmumBlduapBjpdBtjpdp.Bbmc'
    plain = cipher.translate(str.maketrans('BCabcdefghjklmopqstuvxz', ' gvflrscaihkdmpeyntobwu'))
    
    print(plain)
    print()
    print(plain[:25])

if __name__ == '__main__':
    main()
