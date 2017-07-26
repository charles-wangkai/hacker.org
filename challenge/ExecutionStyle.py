#!/usr/bin/env python3

# Q: http://www.hacker.org/challenge/chal.php?id=194
# A: http://www.hacker.org/challenge/chal.php?answer=teddy+bear&id=194&go=Submit

import os.path
import subprocess
import tempfile
import urllib.request
from PIL import Image

def main():
    local_filename = urllib.request.urlretrieve('http://www.hacker.org/challenge/img/Doll2.png')[0]
    image = Image.open(local_filename)
    
    folder = tempfile.tempdir
    
    exe_file = tempfile.NamedTemporaryFile(dir=folder, delete=False)     
    exe_file = open(exe_file.name, 'wb')
    for y in range(image.size[1]):
        for x in range(image.size[0]):
            pixel = image.getpixel((x, y))
            exe_file.write(bytes([pixel]))
    exe_file.close()
     
    subprocess.run(['wine', exe_file.name])

    python_file_name = os.path.join(folder, 'temp.py')
    with open(python_file_name, 'w') as python_file:
        subprocess.run(['perl', os.path.join(folder, 'Doll2.pl')], stdout=python_file)
    
    c_file_name = os.path.join(folder, 'temp.c')
    with open(c_file_name, 'w') as c_file:
        subprocess.run(['python2.7', python_file_name], stdout=c_file)
    
    out_file_name = os.path.join(folder, 'temp.out')
    subprocess.run(['gcc', c_file_name, '-o', out_file_name])
    
    hvm_file_name = os.path.join(folder, 'temp.hvm')
    with open(hvm_file_name, 'w') as hvm_file: 
        subprocess.run([out_file_name], stdout=hvm_file)
        
    subprocess.run(['../hackvm.py', hvm_file_name])

if __name__ == '__main__':
    main()
