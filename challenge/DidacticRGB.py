#!/usr/bin/env python3

# Q: http://www.hacker.org/challenge/chal.php?id=103
# A: http://www.hacker.org/challenge/chal.php?answer=10245318&id=103&go=Submit

import urllib.request
from PIL import Image

def main():
    local_filename = urllib.request.urlretrieve('http://www.hacker.org/challenge/img/didactrgb.png')[0]
    image = Image.open(local_filename)
    
    r, g, b = image.getpixel((0, 0))
    print(r * 256 ** 2 + g * 256 + b)
    
    image.close()

if __name__ == '__main__':
    main()
