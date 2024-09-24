#!/usr/bin/env python3

def fizzbuzz():
    def res():
        for i in range(1, 101):
            if i % 5 == 0:
                yield "Fizz"
            elif (i % 3 == 0):
                yield "Fizz"
            elif (i % 3 == 0 and i % 5 == 0):
                yield "FizzBuzz"
            else:
                yield str(i)

    for result in res():
        print(result, end=' ')
