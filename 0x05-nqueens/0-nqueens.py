#!/usr/bin/python3
""" nqueens """
import sys


if len(sys.argv) > 2 or len(sys.argv) < 2:
    print("Usage: nqueens n")
    exit(1)

if not sys.argv[1].isdigit():
    print("n must be a number")
    exit(1)

if int(sys.argv[1]) < 4:
    print("n must be at least 4")
    exit(1)

n = int(sys.argv[1])


def queens(n, i=0, x=[], y=[], z=[]):
    """ find possible positions """
    if i < n:
        for j in range(n):
            if j not in x and i + j not in y and i - j not in z:
                yield from queens(n, i + 1, x + [j], y + [i + j], z + [i - j])
    else:
        yield x


def solve(n):
    """ solve """
    m = []
    i = 0
    for solution in queens(n, 0):
        for s in solution:
            m.append([i, s])
            i += 1
        print(m)
        m = []
        i = 0


solve(n)
