#!/usr/bin/env python3

# Q: http://www.hacker.org/challenge/chal.php?id=201
# A: http://www.hacker.org/challenge/chal.php?answer=iphone&id=201&go=Submit

# https://en.wikipedia.org/wiki/T9_(predictive_text)

def main():
    KEYLETTER_LIST = [('1', ' '),
                      ('222', 'c'), ('22', 'b'), ('2', 'a'),
                      ('333', 'f'), ('33', 'e'), ('3', 'd'),
                      ('444', 'i'), ('44', 'h'), ('4', 'g'),
                      ('555', 'l'), ('55', 'k'), ('5', 'j'),
                      ('666', 'o'), ('66', 'n'), ('6', 'm'),
                      ('7777', 's'), ('777', 'r'), ('77', 'q'), ('7', 'p'),
                      ('888', 'v'), ('88', 'u'), ('8', 't'),
                      ('9999', 'z'), ('999', 'y'), ('99', 'x'), ('9', 'w'),
                      ('0', '.') ]
    
    keys = '844331266777793377714447777144474466666330'
    while keys:
        for (key, letter) in KEYLETTER_LIST:
            if keys.startswith(key):
                print(letter, end='')
                keys = keys[len(key):]
                break
    
if __name__ == '__main__':
    main()
