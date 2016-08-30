#!/usr/bin/env python3

# Q: http://www.hacker.org/challenge/chal.php?id=297
# A: http://www.hacker.org/challenge/chal.php?answer=noamchomsky&id=297&go=Submit

def A():
    return 'is'

def B():
    return 'mm'

def C():
    return 'oo'

def D():
    return 'rgr'

def E():
    return 'ryg'

def F():
    return 'dth'

def G():
    return 'you'

def H():
    return 'esol'

def I():
    return 'ion' + A()

def J():
    return G() + D() + 'a' + B() + 'ar' + A()

def K():
    return 've' + E() + C() + F() + H() + 'ut' + I()

def L():
    return P() + Q()

def M():
    return 'n'

def N():
    return 'm'

def O():
    return 'oa' + N() + 'cho'

def P():
    return M() + O()

def Q():
    return N() + R()

def R():
    return 'sky'

def S():
    return J() + K() + L()

def main():
    print(S())

if __name__ == '__main__':
    main()
