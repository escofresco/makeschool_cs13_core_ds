#!python

import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    return is_palindrome_recursive(text)
    # return is_palindrome_recursive(text)

def next_letter(text, start, stop, step):
    """Steps through text, finding letters along the way.

    Yields:
        (int) index of next letter in text."""
    for i in range(start, stop, step):
        if (letter := text[i]).isalpha():
            yield i

def is_palindrome_iterative(text):
    left_it = next_letter(text, 0, len(text), 1)
    right_it = next_letter(text, len(text)-1, -1, -1)
    try:
        left_idx = next(left_it)
        right_idx = next(right_it)
    except StopIteration:
        return True
    while left_idx < right_idx:
        if text[left_idx].lower() != text[right_idx].lower():
            return False
        left_idx = next(left_it)
        right_idx = next(right_it)
    return True


def is_palindrome_recursive(text, left=None, right=None):
    """Recursive function for determining if text is a palindrome."""
    if left is right is None:
        ## initialize left and right indices
        return is_palindrome_recursive(text, left=0, right=len(text)-1)
    if left >= right:
        ## Base case: left and right indices have overlapped, text must be a
        ## palindrome
        return True
    if (text[left].isalpha()
        and text[right].isalpha()
        and text[left].lower() != text[right].lower()):
        ## left and right letters aren't equal; text isn't a palindrome
        return False
    if not text[left].isalpha():
        ## left character isn't a letter; move left index to the right by one
        return is_palindrome_recursive(text, left+1, right)
    if not text[right].isalpha():
        ## right character isn't a letter; move right index to the left by one
        return is_palindrome_recursive(text, left, right-1)
    # so far, text is a palindrome
    return is_palindrome_recursive(text, left+1, right-1)

def permutations(arr):
    def recur(i):
        if i == len(arr):
            res.append(arr[:])
        for j in range(len(arr)):
            arr[i], arr[j] = arr[j], arr[i]
            recur(i+1)
            arr[i], arr[j] = arr[j], arr[i]
    res = []
    recur(0)
    return res



def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
