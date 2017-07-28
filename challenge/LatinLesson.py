#!/usr/bin/env python3

# Q: http://www.hacker.org/challenge/chal.php?id=288
# A: http://www.hacker.org/challenge/chal.php?answer=Brian+Cohen&id=288&go=Submit

# https://en.wikipedia.org/wiki/Roman_numerals
# https://en.wikipedia.org/wiki/Romani_ite_domum
# https://en.wikipedia.org/wiki/Monty_Python%27s_Life_of_Brian

SYMBOL_VALUES = [('C', 100), ('XC', 90), ('L', 50), ('XL', 40), ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1)]

def roman_to_char(roman):
    number = 0
    while roman:
        for (symbol, value) in SYMBOL_VALUES:
            if roman.startswith(symbol):
                number += value
                roman = roman[len(symbol):]
    return chr(number)

def main():
    message = 'lxxxiv ci cviii cviii xxxii cix ci xxxii cxvi civ ci xxxii cx xcvii cix ci xxxii cxi cii xxxii cxvi civ ci xxxii cix xcvii cx xxxii cxix civ cxi xxxii cxix cxiv cxi cxvi ci xxxii xxxiv lxxxii cxi cix xcvii cx cv xxxii cv cxvi ci xxxii c cxi cix cxvii cix xxxiv xxxii xlix xlviii xlviii xxxii cxvi cv cix ci cxv xlvi'
    
    print(''.join(map(roman_to_char, message.upper().split(' '))))

if __name__ == '__main__':
    main()
