"""
Stack Data Structure

This is a stack implementation but it isn't the from scratch implementation,
still uses the append + pop methods from a list. To do one better learn how to
implement this from scratch.
"""


class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def get_stack(self):
        return self.items


mystack = Stack()
mystack.push("A")
mystack.push("B")
mystack.push("C")
mystack.push("D")
print(mystack.peek())
