#!/usr/bin/env python3

# Q: http://www.hacker.org/challenge/chal.php?id=107
# A: http://www.hacker.org/challenge/chal.php?answer=ilearnsogood&id=107&go=Submit

import urllib.request
from PIL import Image

def main():
    local_filename = urllib.request.urlretrieve('http://www.hacker.org/challenge/img/greenline.png')[0]
    image = Image.open(local_filename)
    
    print(''.join([chr(image.getpixel((x, 0))[1]) for x in range(image.size[0])]))
    
if __name__ == '__main__':
    main()
