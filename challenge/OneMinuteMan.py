#!/usr/bin/env python3

# Q: http://www.hacker.org/challenge/chal.php?id=116
# A: http://www.hacker.org/challenge/chal.php?answer=gugglemuggle&id=116&go=Submit

# Long run program, so would be better to run on a VPS like Amazon EC2. The web page says "back later" all the time except in one minute a day "i declare the answer is gugglemuggle".

import datetime
import threading
import urllib.request

contents = set()

def check_page():
    source = urllib.request.urlopen('http://www.hacker.org/challenge/misc/minuteman.php').read().decode()
    
    if source not in contents:
        contents.add(source)
        print('[{datetime}]'.format(datetime=datetime.datetime.today()))
        print(source)
        print()
    
    threading.Timer(30, check_page).start()

def main():
    check_page()

if __name__ == '__main__':
    main()
