#!usr/bin/env python3
# encoding=utf-8


def equals(str1, str2):
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise TypeError('arguments type must be <str>')
    if str1 == str2:
        return True
    return False


def is_empty(string):
    if not isinstance(string, str):
        raise TypeError('arguments type must be <str>')

    if not string:
        return True
    return False
