#!/usr/bin/env python3

# Q: http://www.hacker.org/challenge/chal.php?id=52
# A: http://www.hacker.org/challenge/chal.php?answer=etch&id=52&go=Submit

# https://en.wikipedia.org/wiki/Etch_A_Sketch

import re
import urllib.request
from PIL import Image
import hacker_org_util

PROBLEM_ID = '52'

def main():
    source = urllib.request.urlopen(hacker_org_util.build_challenge_url(PROBLEM_ID)).read().decode()
    
    directions = re.findall(r'(?<=<img src="img/.).(?=.\.gif">)', source, flags=re.DOTALL)
    
    out_image = Image.new('1', (300, 30))
    
    x, y = 10, 10
    out_image.putpixel((x, y), 1)
    for direction in directions:
        for _ in range(5):
            if direction == 'u':
                y -= 1
            elif direction == 'r':
                x += 1
            elif direction == 'd':
                y += 1
            else:
                x -= 1
            
            out_image.putpixel((x, y), 1)
    
    out_image.show()
    out_image.close()

if __name__ == '__main__':
    main()
