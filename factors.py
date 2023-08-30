#!/usr/bin/python3
import sys
import random
from math import gcd


def pollards_rho(n):
    x = random.randint(1, n - 1)
    y = x
    d = 1
    f = lambda x: (x * x + 1) % n
    while d == 1:
        x = f(x)
        y = f(f(y))
        d = gcd(abs(x - y), n)

    return d

def main(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            n = int(line.strip())
            factors = pollards_rho(n)
            print("{}={}*{}".format(n, n // factors, factors))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("factors <file>")
        sys.exit(1)

    file_input = sys.argv[1]
    main(file_input)
