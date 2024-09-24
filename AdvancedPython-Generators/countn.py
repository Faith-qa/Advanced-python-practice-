#!/usr/bin/env python3
def count_up_to(n):
    y = 1
    while y < n+1:
        yield y
        y += 1
