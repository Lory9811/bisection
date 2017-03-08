#!/usr/bin/env python
import sys
from numpy import *

def calculate(function, r, p, res):
    a, b = str.split(r, ';')
    a, b, p, res = int(a), int(b), int(p), int(res)
    function = str.replace(function, '^', '**')

    for i in range(p + 1):
        x = a
        fa = eval(function)
        x = b
        fb = eval(function)
        m = (a + b) / 2
        x = m
        fm = eval(function)
        print("{0}: a:{1}, b:{2}, m:{3}, f(a):{4}, f(b):{5}, f(m):{6}"
              .format(i, a, b, m, fa, fb, fm))
        if fm == 0 or abs(fm) < res and res != 0:
            print("Done!")
            break
        if sign(fm) == sign(fa):
            a = m
        else: b = m

def main():
    print("Warning: 'Function' parameter is dangerous: the string is just eval()'d")
    input_str = input("Function, range, passes, optional: resolution (0 to disable):")
    try:
        fn, rn, p, res = str.split(input_str, ',')
    except ValueError:
        print("Not enough/too many parameters, expected 4")
        sys.exit(-42)
    calculate(fn, rn, p, res)
    if sys.platform == 'win32':
        input("Press 'Return' to exit")
    sys.exit(0)

if __name__ == '__main__':
    main()