#!/usr/bin/env python3

# Q: http://www.hacker.org/challenge/chal.php?id=164
# A: http://www.hacker.org/challenge/chal.php?answer=pourcoffee&id=164&go=Submit

import html

def main():
    msg = '&#38&#119&#101&#105&#101&#114&#112&#59&#38&#79&#116&#105&#108&#100&#101&#59&#38&#85&#103&#114&#97&#118&#101&#59&#38&#114&#101&#97&#108&#59&#38&#99&#111&#112&#121&#59&#38&#84&#104&#101&#116&#97&#59&#38&#102&#110&#111&#102&#59&#38&#102&#110&#111&#102&#59&#38&#105&#115&#105&#110&#59&#38&#105&#115&#105&#110&#59'
    print(html.unescape(html.unescape(msg)))

if __name__ == '__main__':
    main()
