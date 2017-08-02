#!/usr/bin/env python3

# Q: http://www.hacker.org/challenge/chal.php?id=108
# A: http://www.hacker.org/challenge/chal.php?answer=1936264348&id=108&go=Submit

# Use a C# decompiler (dotPeek: https://www.jetbrains.com/decompiler/) to see the source code of the exe file (http://www.hacker.org/challenge/misc/Sharper.exe).
#
# The original C# code:
#
# using System;
# 
# namespace Sharper
# {
#   internal class Program
#   {
#     private static void Main(string[] args)
#     {
#       Console.WriteLine("calculating...");
#       int num = 99;
#       for (int index = num; index >= 0; --index)
#       {
#         Console.WriteLine(index);
#         Console.WriteLine("val: " + Program.calc(num - index).ToString());
#       }
#     }
# 
#     private static int calc(int num)
#     {
#       int num1 = 0;
#       for (int index1 = 0; index1 < num; ++index1)
#       {
#         for (int index2 = 0; index2 < num; ++index2)
#         {
#           for (int index3 = 0; index3 < num; ++index3)
#           {
#             for (int index4 = 0; index4 < num; ++index4)
#             {
#               for (int index5 = 0; index5 < num; ++index5)
#               {
#                 string str = index1.ToString() + " to " + index2.ToString() + " to " + index3.ToString() + " to " + index4.ToString() + " to " + index5.ToString();
#                 num1 += str.Length;
#               }
#             }
#           }
#         }
#       }
#       return num1;
#     }
#   }
# }

def int_overflow(val, maxint):
    if not -maxint - 1 <= val <= maxint:
        val = (val + (maxint + 1)) % (2 * (maxint + 1)) - (maxint + 1)
    return val
  
def main():
    num = 99
    result = len(' to ') * 4 * (num ** 5)
    
    for i in range(num):
        result += len(str(i)) * (num ** 4) * 5
    
    print(int_overflow(result, (1 << 31) - 1))

if __name__ == '__main__':
    main()
