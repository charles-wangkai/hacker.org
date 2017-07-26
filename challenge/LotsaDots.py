#!/usr/bin/env python3

# Q: http://www.hacker.org/challenge/chal.php?id=79
# A: (Not fixed answer, so run this script)

import urllib.request
from PIL import Image
import hacker_org_util

PROBLEM_ID = '79'

def main():
    urllib.request.urlopen(hacker_org_util.build_challenge_url(PROBLEM_ID))
    
    local_filename = urllib.request.urlretrieve('http://www.hacker.org/challenge/misc/stars.php')[0]
    image = Image.open(local_filename)
    
    answer = ''
    for y in range(8, image.size[1], 16):
        answer += chr(int(''.join(map(lambda x: '1' if image.getpixel((x, y)) == (230, 230, 230) else '0', range(8, image.size[0], 16))), base=2))
    print(answer)

    print(urllib.request.urlopen(hacker_org_util.build_challenge_url(PROBLEM_ID, answer)).read().decode())

if __name__ == '__main__':
    main()
