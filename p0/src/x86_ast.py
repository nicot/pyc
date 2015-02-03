#!/usr/bin/env python
class x86ast:
    class mov:
        def __init__(self, src, dest):
            self.src = src
            self.dest = dest

        def __repr__(self):
            return "mov " +  self.src + ", " +  self.dest

    class pushl:
        def __init__(self, operand):
            self.operand = operand

        def __repr__(self):
            return "pushl " + self.operand

    class addl:
        def __init__(self, left, right):
            self.left = left
            self.right = right

        def __repr__(self):
            return "addl " + self.left + ", " + self.right


a = x86ast.mov('a', 'b')
a.src = 'asdf'
print a
