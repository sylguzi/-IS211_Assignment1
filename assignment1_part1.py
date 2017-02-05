#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""assignment1_part1."""


def listDivide(numbers, divide=2):
    """Divides a provided list with a default of 2.
    Args:
        numbers (list): list of numbers
        divide (int): the number being devided by; default is 2

    Returns:
        int: number of digits that are divisible by divide.

    Examples:
        >>>listDivide([30, 54, 63,98, 100], divide=10)
           2
    """
    count = []
    for num in numbers:
        if num % divide == 0:
            count.append(num)
    return len(count)


class ListDivideException(Exception):
    def __init__(self, msg):

        self.msg = msg


def testListDivide():
    """Tests listDivide against examples listed in runs.

    If everything functions properly, no returns. If something goes awry,
    an error will be displayed.
    """

    runs = [([1,2,3,4,5],2,2), ([2,4,6,8,10],2,5), ([30,54,63,98,100],10,2),
    ([],2,0), ([1,2,3,4,5],1,5)]
    for n in runs:
        if listDivide(n[0], n[1]) != n[2]:
            raise ListDivideException("fail")


if __name__ == 'main':
    testListDivide()
