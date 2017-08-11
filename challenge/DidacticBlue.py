#!/usr/bin/env python3

# Q: http://www.hacker.org/challenge/chal.php?id=272
# A: http://www.hacker.org/challenge/chal.php?answer=case&id=272&go=Submit

import urllib.request
from PIL import Image

def main():
    local_filename = urllib.request.urlretrieve('http://www.hacker.org/challenge/img/blue.png')[0]
    image = Image.open(local_filename)
    
    width, height = image.size
    lines = []
    for y in range(height):
        line = ''
        for x in range(width):
            line += chr(image.getpixel((x, y))[2])
        lines.append(line)
    
    for line in lines[::-1]:
        print(line)
    
    image.close()

if __name__ == '__main__':
    main()
