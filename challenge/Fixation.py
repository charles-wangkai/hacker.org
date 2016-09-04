#!/usr/bin/env python3

# Q: http://www.hacker.org/challenge/chal.php?id=88
# A: http://www.hacker.org/challenge/chal.php?answer=snugglefish&id=88&go=Submit

import urllib.request
from PIL import Image

def main():
    local_filename = urllib.request.urlretrieve('http://www.hacker.org/challenge/img/swirl.gif')[0]
    image = Image.open(local_filename)
    
    while True:
        try:
            image.seek(image.tell() + 1)
        except EOFError:
            break
        image.show()
    
    image.close()
    
if __name__ == '__main__':
    main()
