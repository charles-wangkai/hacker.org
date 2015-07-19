#!/usr/bin/env python3

# Q: http://www.hacker.org/challenge/chal.php?id=31
# A: http://www.hacker.org/challenge/chal.php?answer=soundofsilence&id=31&go=Submit

# https://en.wikipedia.org/wiki/Braille

CODE2LETTER = {
'''\
  
  
  \
''': ' ',
'''\
. 
  
  \
''': 'a',
'''\
. 
. 
  \
''': 'b',
'''\
..
  
  \
''': 'c',
'''\
..
 .
  \
''': 'd',
'''\
. 
 .
  \
''': 'e',
'''\
..
. 
  \
''': 'f',
'''\
..
..
  \
''': 'g',
'''\
. 
..
  \
''': 'h',
'''\
 .
. 
  \
''': 'i',
'''\
 .
..
  \
''': 'j',
'''\
. 
  
. \
''': 'k',
'''\
. 
. 
. \
''': 'l',
'''\
..
  
. \
''': 'm',
'''\
..
 .
. \
''': 'n',
'''\
. 
 .
. \
''': 'o',
'''\
..
. 
. \
''': 'p',
'''\
..
..
. \
''': 'q',
'''\
. 
..
. \
''': 'r',
'''\
 .
. 
. \
''': 's',
'''\
 .
..
. \
''': 't',
'''\
. 
  
..\
''': 'u',
'''\
. 
. 
..\
''': 'v',
'''\
 .
..
 .\
''': 'w',
'''\
..
  
..\
''': 'x',
'''\
..
 .
..\
''': 'y',
'''\
. 
 .
..\
''': 'z'}

def separate(message):
    return list(map('\n'.join, zip(*map(lambda line: [line[i:i + 2] for i in range(0, len(line), 3)], message.split(sep='\n')))))

def main():
    message = '''\
 . .  .     .  ..  .  . .  .      .  .     . .  .  .. .. .  ..  .  . .  .  .. .. .  
.. ..  .        . .  ..  . ..    .  .     .   .     .  .  . .  .  .  .   .  .     . 
.              .  .   .    .        .     .  .  .. .     .     .     .     .        \
'''
    print(''.join(map(CODE2LETTER.get, separate(message))))

if __name__ == '__main__':
    main()
