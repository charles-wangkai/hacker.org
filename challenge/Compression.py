#!/usr/bin/env python3

# Q: http://www.hacker.org/challenge/chal.php?id=83
# A: http://www.hacker.org/challenge/chal.php?answer=eggnogpudding&id=83&go=Submit

import binhex
import os
import subprocess
import tempfile
import urllib.request
import pyunpack

def get_regular_filename(folder):
    for name in os.listdir(folder):
        if not name.startswith('.') and os.path.isfile(os.path.join(folder, name)):
            return name

def main():
    folder = tempfile.gettempdir()
    
    local_filename = urllib.request.urlretrieve('http://www.hacker.org/challenge/misc/file.compressed')[0]
    
    zip_file = pyunpack.Archive(local_filename)
    folder += '/rar'
    zip_file.extractall(folder, auto_create_dir=True)
    rar_filename = get_regular_filename(folder)

    rar_file = pyunpack.Archive(os.path.join(folder, rar_filename))
    folder += '/arj'
    rar_file.extractall(folder, auto_create_dir=True)
    arj_filename = get_regular_filename(folder)
    
    arj_file = pyunpack.Archive(os.path.join(folder, arj_filename))
    folder += '/cab'
    arj_file.extractall(folder, auto_create_dir=True)
    cab_filename = get_regular_filename(folder)
    
    cab_file = pyunpack.Archive(os.path.join(folder, cab_filename))
    folder += '/hqx'
    cab_file.extractall(folder, auto_create_dir=True)
    hqx_filename = get_regular_filename(folder)
    
    hqx_path = os.path.join(folder, hqx_filename)
    folder += '/sitx'
    os.makedirs(folder, exist_ok=True)
    os.chdir(folder)
    binhex.hexbin(hqx_path, None)
    sitx_filename = get_regular_filename(folder)

    sitx_path = os.path.join(folder, sitx_filename)
    folder += '/gz'
    os.makedirs(folder, exist_ok=True)
    os.chdir(folder)
    subprocess.run(['unar', '-f', sitx_path], stdout=open(os.devnull, 'w'))
    gz_filename = get_regular_filename(folder)
    
    gz_file = pyunpack.Archive(os.path.join(folder, gz_filename))
    folder += '/bz2'
    gz_file.extractall(folder, auto_create_dir=True)
    bz2_filename = get_regular_filename(folder)
    
    bz2_file = pyunpack.Archive(os.path.join(folder, bz2_filename))
    folder += '/7z'
    bz2_file.extractall(folder, auto_create_dir=True)
    _7z_filename = get_regular_filename(folder)
    
    _7z_file = pyunpack.Archive(os.path.join(folder, _7z_filename))
    folder += '/txt'
    _7z_file.extractall(folder, auto_create_dir=True)
    txt_filename = get_regular_filename(folder)
    
    print(open(os.path.join(folder, txt_filename)).read())

if __name__ == '__main__':
    main()
