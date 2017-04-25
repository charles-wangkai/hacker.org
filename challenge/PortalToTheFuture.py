#!/usr/bin/env python3

# Q: http://www.hacker.org/challenge/chal.php?id=100
# A: http://www.hacker.org/challenge/chal.php?answer=999696&id=100&go=Submit

# http://stackoverflow.com/questions/1293308/java-api-to-find-out-the-jdk-version-a-class-file-is-compiled-for/5571374#5571374

import binascii
import subprocess
import tempfile
import urllib.request

def main():
    CLASS_NAME = 'PrintThatNumber'
    
    local_filename = urllib.request.urlretrieve('http://www.hacker.org/challenge/misc/' + CLASS_NAME + '.class')[0]

    content = open(local_filename, 'rb').read()
    print(binascii.hexlify(content[:8]).decode())

    fixed_content = content[:7] + bytes([50]) + content[8:]
    print(binascii.hexlify(fixed_content[:8]).decode())

    temp_dir = tempfile.gettempdir()
    fixed_filename = temp_dir + '/' + CLASS_NAME + '.class'
    open(fixed_filename, 'wb').write(fixed_content)
    
    subprocess.call(['java', '-cp', temp_dir, CLASS_NAME])

if __name__ == '__main__':
    main()
