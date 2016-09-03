#!/usr/bin/env python3

# Q: http://www.hacker.org/challenge/chal.php?id=136
# A: http://www.hacker.org/challenge/chal.php?answer=adumbrate&id=136&go=Submit

def main():
    s = 'abbbabaaabbabaaaabbaababaabaaaaaabbaaaababbabbbaabbbaabbabbbabbbabbaabababbbaabaaabaaaaaabbabaababbbaabbaabaaaaaabbaaaababbaabaaabbbabababbabbababbaaabaabbbaabaabbaaaababbbabaaabbaabab'
    
    n = int(s.translate(str.maketrans('ab', '01')), 2)
    print(n.to_bytes((n.bit_length() + 7) // 8, 'big').decode())

if __name__ == '__main__':
    main()
