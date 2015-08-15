#!/usr/bin/env python

import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..', '..'))

import hackvm

def main():
    hackvm.run(MAX_CYCLES=100000)

if __name__ == '__main__':
    main()
