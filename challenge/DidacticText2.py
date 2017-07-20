#!/usr/bin/env python3

# Q: http://www.hacker.org/challenge/chal.php?id=130
# A: http://www.hacker.org/challenge/chal.php?answer=dinosoreass&id=130&go=Submit

# The 11 sentences are from Bible. Find their chapters and locations as follows, then convert each of the second numbers to a letter.
# http://biblehub.com/deuteronomy/8-4.htm
# http://biblehub.com/deuteronomy/20-9.htm
# http://biblehub.com/deuteronomy/21-14.htm
# http://biblehub.com/deuteronomy/26-15.htm
# http://biblehub.com/deuteronomy/31-19.htm
# http://biblehub.com/deuteronomy/32-15.htm
# http://biblehub.com/deuteronomy/1-18.htm
# http://biblehub.com/deuteronomy/24-5.htm
# http://biblehub.com/deuteronomy/24-1.htm
# http://biblehub.com/deuteronomy/33-19.htm
# http://biblehub.com/deuteronomy/28-19.htm

def main():
    locations = [4, 9, 14, 15, 19, 15, 18, 5, 1, 19, 19]
    print(''.join(map(lambda location: chr(ord('a') - 1 + location), locations)))

if __name__ == '__main__':
    main()
