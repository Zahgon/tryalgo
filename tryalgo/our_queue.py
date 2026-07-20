#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class OurQueue:
    def __init__(self):
        self.in_stack = []        # tail
        self.out_stack = []       # head

    def __len__(self):
        return len(self.in_stack) + len(self.out_stack)

    def push(self, obj):
        pass

    def pop(self):
        if not self.out_stack:    # head is empty
            self.out_stack = self.in_stack[::-1]
            self.in_stack = []
        return self.out_stack.pop()

    def __str__(self):
        return str(self.out_stack[::-1] + self.in_stack)
