#!/usr/bin/env python3

# Q: http://www.hacker.org/challenge/chal.php?id=45
# A: http://www.hacker.org/challenge/chal.php?answer=1234&id=45&go=Submit

import subprocess
import tempfile
import urllib.request
from PIL import Image

def main():
    local_filename = urllib.request.urlretrieve('http://www.hacker.org/challenge/img/listen.png')[0]
    image = Image.open(local_filename)
    
    mp3_file = tempfile.NamedTemporaryFile(delete=False)
    
    mp3_file = open(mp3_file.name, 'wb')
    for y in range(image.size[1]):
        for x in range(image.size[0]):
            pixel = image.getpixel((x, y))
            mp3_file.write(bytes([pixel[0]]))
            mp3_file.write(bytes([pixel[1]]))
            mp3_file.write(bytes([pixel[2]]))
     
    subprocess.run(['afplay', mp3_file.name])

if __name__ == '__main__':
    main()
