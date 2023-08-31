#!/usr/bin/python3
import sys
from math import gcd


def pollards_rho(n):
    x = 2
    y = 2
    d = 1

    f = lambda x: (x ** 2 + 1) % n

    while d == 1:
        x = f(x)
        y = f(f(y))
        d = gcd(abs(x - y), n)

    return d, n // d


def main(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            n = int(line.strip())
            factor1, factor2 = pollards_rho(n)
            print("{}={}*{}".format(n, factor1, factor2))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("factors <file>")
        sys.exit(1)

    file_input = sys.argv[1]
    main(file_input)
