#!/usr/bin/env python3

# Q: http://www.hacker.org/challenge/chal.php?id=20
# A: http://www.hacker.org/challenge/chal.php?answer=madreup&id=20&go=Submit

import urllib.request

class Log302_HTTPRedirectHandler(urllib.request.HTTPRedirectHandler):
    def http_error_302(self, req, fp, code, msg, hdrs):
        print(hdrs['X-hacker-answer'])
        return super().http_error_302(req, fp, code, msg, hdrs)

def main():
    opener = urllib.request.build_opener(Log302_HTTPRedirectHandler())
    urllib.request.install_opener(opener)
    
    urllib.request.urlopen('http://www.hacker.org/challenge/misc/one.php')

if __name__ == '__main__':
    main()
