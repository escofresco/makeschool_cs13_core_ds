#!python
from collections import deque
from functools import reduce

import string
# Hint: Use these string constants to encode/decode hexadecimal digits and mor
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace


def decode(
        digits,
        base,
        char_to_digit={
            **{str(i): i
               for i in range(10)},
            **{
                chr(i + ord('a')): i + 10
                for i in range(ord('z') + 1 - ord('a'))
            }
        }):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)

    return reduce(
        lambda x, y: (x[0] - 1, x[1] + char_to_digit[y] * base**(x[0])),
        digits, (len(digits) - 1, 0))[1]


def encode(
        number,
        base,
        digit_to_char={
            **{i: str(i)
               for i in range(10)},
            **{
                i + 10: chr(i + ord('a'))
                for i in range(ord('z') + 1 - ord('a'))
            }
        }):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)
    res = deque()

    while number > 0:
        number, remainder = divmod(number, base)
        # res.appendleft(str(remainder))
        res.appendleft(digit_to_char.get(remainder))
    return ''.join(res)


def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    char_to_digit = {str(i): i for i in range(10)}
    char_to_digit.update(
        {chr(i + ord('a')): i + 10
         for i in range(ord('z') + 1 - ord('a'))})
    digit_to_char = {v: k for k, v in char_to_digit.items()}
    return encode(decode(digits, base1, char_to_digit), base2, digit_to_char)


def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result,
                                                      base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    main()
