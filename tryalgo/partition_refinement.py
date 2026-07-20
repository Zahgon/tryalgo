#!/usr/bin/env python3
# -*- coding: utf-8 -*-


__all__ = ["PartitionRefinement"]


class DoubleLinkedListItem:

    def __init__(self, anchor=None):
        """Create a new item to be inserted before item anchor.
           if anchor is None: create a single item circular double linked list
        """
        if anchor:
            self.insert(anchor)
        else:
            self.prec = self
            self.succ = self

    def remove(self):
        self.prec.succ = self.succ
        self.succ.prec = self.prec

    def insert(self, anchor):
        """insert list item before anchor
        """
        self.prec = anchor.prec        # point to neighbors
        self.succ = anchor
        self.succ.prec = self          # make neighbors point to item
        self.prec.succ = self

    def __iter__(self):
        """iterate trough circular list.
        warning: might end stuck in an infinite loop if chaining is not valid
        """
        curr = self
        yield self
        while curr.succ != self:
            curr = curr.succ
            yield curr


class PartitionClass(DoubleLinkedListItem):

    def __init__(self, anchor=None):
        DoubleLinkedListItem.__init__(self, anchor)
        self.items = None         # empty list
        self.split = None         # reference to split class

    def append(self, item):
        """add item to the end of the item list
        """
        if not self.items:        # was list empty ?
            self.items = item     # then this is the new head
        item.insert(self.items)


class PartitionItem(DoubleLinkedListItem):

    def __init__(self, val, theclass):
        DoubleLinkedListItem.__init__(self)
        self.val = val
        self.theclass = theclass
        theclass.append(self)

    def remove(self):
        """remove item from its class
        """
        DoubleLinkedListItem.remove(self)     # remove from double linked list
        if self.succ is self:                 # list was a singleton
            self.theclass.items = None        # class is empty
        elif self.theclass.items is self:     # oups we removed the head
            self.theclass.items = self.succ   # head is now successor


class PartitionRefinement:

    def __init__(self, n):
        """Start with the partition consisting of the unique class {0,1,..,n-1}
        complexity: O(n) both in time and space
        """
        c = PartitionClass()   # initially there is a single class of size n
        self.classes = c       # reference to first class in class list
        self.items = [PartitionItem(i, c) for i in range(n)]  # value-ordered

    def refine(self, pivot):
        pass

    def tolist(self):
        pass

    def order(self):
        pass
