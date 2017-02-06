#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""assignment1_part2."""

class Book(object): #reminder - self MUST be 1st arg of any funct in class


    author = ''
    title = ''

    def __init__(self, author, title):
        """Takes an author and a title, sets them to the object variables"""

        self.author = author
        self.title = title

    
    def display(self):
        """Prints out a string representing the book
        """

        result = "{}, written by {}.".format(self.title, self.author)
        print result

omam = Book('John Steinbeck', 'Of Mice and Men')
tkam = Book('Harper Lee', 'To Kill A Mocking Bird')

omam.display()
tkam.display()
