#!/usr/bin/env python3

# Q: http://www.hacker.org/challenge/chal.php?id=28
# A: http://www.hacker.org/challenge/chal.php?answer=hoarse&id=28&go=Submit

# https://en.wikipedia.org/wiki/Morse_code

CODE2LETTER = {'.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e', '..-.': 'f', '--.': 'g', '....': 'h', '..': 'i', '.---': 'j', '-.-': 'k', '.-..': 'l', '--': 'm', '-.': 'n', '---': 'o', '.--.': 'p', '--.-': 'q', '.-.': 'r', '...': 's', '-': 't', '..-': 'u', '...-': 'v', '.--': 'w', '-..-': 'x', '-.--': 'y', '--..': 'z'}

def main():
    message = '- .... . .- -. ... .-- . .-. .. ... .... --- .- .-. ... .'
    print(''.join(map(CODE2LETTER.get, message.split())))

if __name__ == '__main__':
    main()
