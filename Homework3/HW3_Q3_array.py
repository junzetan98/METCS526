# Use recursion and make a function to reverse a stack implemented as an array

# Define the stack class using an array
class Stack:
    def __init__(self):
        self.items = [] # Use a list (a dynamic array) to implement the stack

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from empty stack")

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

# Create a second stack to hold the reversed elements
stack_2 = Stack()

# Create a recursive function to reverse stack
def reverse_stack(stack):
    if stack.is_empty():
        return
    
    top = stack.pop()
    stack_2.push(top)
    return reverse_stack(stack)


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
    print('Stack Items Type:', type(stack.items))
    reverse_stack(stack)
    print('Reversed Stack:', stack_2)



if __name__ == "__main__":
    main()