# Q2: 
# Build the function doIt(node) that prints the values of a linked list in reverse order.
def doIt(node):
    if node is None:
        return 
    doIt(node.next)
    print(node.value)

# Create a linked list with 12, 3, 5, 2 as values
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Create nodes
n1 = Node(12)
n2 = Node(3)    
n3 = Node(5)
n4 = Node(2)

# Link them
n1.next = n2
n2.next = n3
n3.next = n4
ll = n1

print("Q2 Answer is:")
doIt(ll)

# Q3: Building the function doIt(n) as described below and print the outputs of doIt(1), doIt(3), and doIt(6).
def doIt(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return doIt(n-1) + doIt(n-2) - doIt(n-3)

print("Q3 Answers are:")
print(doIt(1))
print(doIt(3))
print(doIt(6))

# Q4: Build a function to find the sum of three middle nodes in a odd-length doubly linked list.
# 1. Build a doubly linked list
class DNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = DNode(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

# Build an example doubly linked list with odd length
dll = DoublyLinkedList()
for i in range(1, 10):  # Create a list with values from 1 to 9
    dll.append(i)

def print_doubly_ll(dll):
    current = dll.head
    while current:
        print(current.value, end=" <-> ")
        current = current.next
    print("None")

print("Q4 - Doubly Linked List Example:")
print_doubly_ll(dll)


# Q4: 
# 2. Design a function to find the sum of the three middle nodes in an odd-length doubly linked list.
def sum_of_three_middle_nodes(dll):
    if dll.head is None or dll.tail is None:
        return 0

    slow = dll.head
    fast = dll.head

    # Use the two-pointer technique to find the middle node
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    # Now, 'slow' is at the middle node
    middle_value = slow.value
    prev_value = slow.prev.value if slow.prev else 0
    next_value = slow.next.value if slow.next else 0

    return middle_value + prev_value + next_value

# Test example list
result = sum_of_three_middle_nodes(dll)

print("Q4 - Sum of three middle nodes (Example):", result)

