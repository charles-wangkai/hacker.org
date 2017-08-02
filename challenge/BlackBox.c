// Q: http://www.hacker.org/challenge/chal.php?id=110
// A: http://www.hacker.org/challenge/chal.php?answer=1982222004&id=110&go=Submit

// Use a decompiler (Retargetable Decompilation: https://retdec.com/decompilation/) to see the source code of the file (http://www.hacker.org/challenge/misc/onetest).

// The original C code:

// #include <stdint.h>
// #include <stdio.h>
// #include <stdlib.h>

// int main(int argc, char ** argv) {
//     uint32_t str_as_i = atoi((char *)*(int32_t *)((int32_t)argv + 4));
//     return printf("%d\n", 0x1534162 * ((str_as_i & str_as_i / 0x80000000 - 1) - 0x6fe5d5 ^ 0x2eb22189) ^ 0x69f6bc7);
// }


#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char ** argv) {
    for (uint32_t str_as_i = 0;; str_as_i++) {
        if ((0x1534162 * ((str_as_i & str_as_i / 0x80000000 - 1) - 0x6fe5d5 ^ 0x2eb22189) ^ 0x69f6bc7) == 230392619) {
            printf("%d\n", str_as_i);
            break;
        }
    }
}
