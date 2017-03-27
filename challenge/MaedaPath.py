#!/usr/bin/env python3

# Q: http://www.hacker.org/challenge/chal.php?id=41
# A: http://www.hacker.org/challenge/chal.php?answer=156145&id=41&go=Submit

# 1) Download the Flash file (http://www.hacker.org/challenge/misc/maeda.swf).
# 2) Use a Flash decompiler (e.g. JPEXS Free Flash Decompiler, https://www.free-decompiler.com/flash/).
# 3) Search text "a n s w e r", then find the ActionScript source snippet: "/DefineSprite (91)/frame 2/DoAction"

def main():
    xx = 18
    aa = 17
    xx = xx * (29 * aa)
    xx = xx + (5423 + aa)
    xx = xx * 11
    xx = xx - 77 * aa
    print(xx)

if __name__ == '__main__':
    main()
