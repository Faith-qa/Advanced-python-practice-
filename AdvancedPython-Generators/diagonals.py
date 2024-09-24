#!/usr/bin/env python3

def print_diagonal(n):
    if n <= 0:
        print("\n", end='')
    else:
        lines = (' ' * i + '\\' for i in range(n))
        return lines