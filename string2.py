#!/usr/bin/env python3
"""
Kenzie assignment: String2
"""
# Your name, plus anyone who helped you with this assignment.
# Give credit where credit is due.
__author__ = "goddesscoder"

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Instructions:
# Complete each of these string exercises in the same way as the
# previous String1 excercises.

# D. verbing
# Given a string, if its length is at least 3, add 'ing' to its
# end unless it already ends in 'ing', in which case add 'ly'
# instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.


def verbing(s):
    # your code here
    string = s
    if len(string) >= 3 and string.endswith("ing"):
        return string + "ly"
    elif len(string) < 3:
        return string
    else:
        return string + "ing"


# E. not_bad
# Given a string, find the first occurrence of the substrings
# 'not' and 'bad'. If the 'bad' follows the 'not', replace
# the whole 'not'...'bad' substring with 'good'.
# Return the resulting string.
# Example:
#   'This dinner is not that bad!' -> 'This dinner is good!'


def not_bad(s):
    # your code here
    e_string = s
    e_not = e_string.find("not")
    e_bad = e_string.find("bad")
    e_notbad = e_string.split("not")[0]

    if (e_bad > e_not):
        if e_string[-1] in ("!"):
            return e_notbad + "good!"
        return e_notbad + "good"
    else:
        return e_string


# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same
# length. If the length is odd, we'll say that the extra
# character goes in the front half.
#   e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form:
#   a-front + b-front + a-back + b-back


def front_back(a, b):
    # your code here
    # joint_stringnum = len(a) + len(b)
    # joint_string = a + b
    string_a = a
    string_b = b

    if len(string_a) % 2 == 0:
        a_front = a[:len(a)//2]
        a_back = a[len(a)//2:]
    else:
        a_front = a[:len(a)//2+1]
        a_back = a[len(a)//2+1:]
    if len(string_b) % 2 == 0:
        b_front = b[:len(b)//2]
        b_back = b[len(b)//2:]
    else:
        b_front = b[:len(b)//2+1]
        b_back = b[len(b)//2+1:]

    return a_front + b_front + a_back + b_back


# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {}     expected: {}'.format(
        prefix,
        repr(got),
        repr(expected)))


# The main() function calls the above functions with interesting
# inputs, using test() to check whether each result is correct or not.
def main():
    # Each line calls one of the functions above and compares its
    # result to the expected return value for that call.

    print('verbing')
    test(verbing('hail'), 'hailing')
    test(verbing('swimming'), 'swimmingly')
    test(verbing('do'), 'do')

    print('\nnot_bad')
    test(not_bad('This movie is not so bad'), 'This movie is good')
    test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
    test(not_bad('This tea is not hot'), 'This tea is not hot')
    test(not_bad("It's bad yet not"), "It's bad yet not")

    print('\nfront_back')
    test(front_back('abcd', 'xy'), 'abxcdy')
    test(front_back('abcde', 'xyz'), 'abcxydez')
    test(front_back('Kitten', 'Donut'), 'KitDontenut')


# Standard boilerplate (python idiom) to call the main() function.
# This is called an "import guard".
if __name__ == '__main__':
    main()
