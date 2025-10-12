# Use recursion and make a function to reverse a stack implemented as a linked list
# Define the node class for linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None   

# Define the stack class using linked list
class Stack:
    def __init__(self):
        self.top = None  # Top of the stack
        self._size = 0   # Keep track of size

    def is_empty(self):
        return self.top is None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        self._size += 1

    def pop(self):
        if not self.is_empty():
            popped_value = self.top.value
            self.top = self.top.next
            return popped_value
        else:
            raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.top.value
        else:
            raise IndexError("peek from empty stack")

    def size(self):
        return self._size

    def __str__(self):
        values = []
        current = self.top
        while current:
            values.append(current.value)
            current = current.next
        return " → ".join(values)


# Define the recursive function to reverse stack
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
def main():
    stack = Stack()
    import re

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