#!/usr/bin/env python3

# Q: http://www.hacker.org/challenge/chal.php?id=104
# A: http://www.hacker.org/challenge/chal.php?answer=defaced1&id=104&go=Submit

import urllib.request
from PIL import Image

def main():
    local_filename = urllib.request.urlretrieve('http://www.hacker.org/challenge/img/redline.png')[0]
    image = Image.open(local_filename)
    
    print(''.join([hex(image.getpixel((x, 0))[0])[2:] for x in range(4)]))
    
    image.close()

if __name__ == '__main__':
    main()
