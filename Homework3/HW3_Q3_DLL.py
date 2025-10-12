# Use recursion and make a function to reverse a stack implemented as a doubly linked list

# Define the node class for doubly linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None  # new pointer to the previous node


# Define the stack class using a doubly linked list
class Stack:
    def __init__(self):
        self.top = None     # Top of the stack
        self.bottom = None  
        self._size = 0

    def is_empty(self):
        return self.top is None

    def push(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.top = self.bottom = new_node
        else:
            new_node.next = self.top
            self.top.prev = new_node
            self.top = new_node
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        popped_value = self.top.value
        self.top = self.top.next
        if self.top:  # if not empty now
            self.top.prev = None
        else:
            self.bottom = None  # stack became empty
        self._size -= 1
        return popped_value

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.top.value

    def size(self):
        return self._size

    def __str__(self):
        values = []
        current = self.top
        while current:
            values.append(str(current.value))
            current = current.next
        return " ↔ ".join(values)  


# Recursive function to reverse a doubly linked list stack
def reverse_stack(stack, reversed_stack=None):
    if reversed_stack is None:
        reversed_stack = Stack()
    
    if stack.is_empty():
        return reversed_stack
    
    top = stack.pop()
    reversed_stack.push(top)
    return reverse_stack(stack, reversed_stack)


# Read input from standard input and push each line onto the stack
import sys
import re

def main():
    stack = Stack()

    for line in sys.stdin:
        line = line.strip()
        # Use regex to split by either comma or space
        elements = re.split(r'[,\s]+', line)
        for el in elements:
            if el:  # skip empty strings
                stack.push(el)
    
    print('Original Stack:', stack)
    reversed_stack = reverse_stack(stack)
    print('Reversed Stack:', reversed_stack)


if __name__ == "__main__":
    main()