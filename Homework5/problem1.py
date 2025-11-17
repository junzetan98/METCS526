# implement a binary search tree
# create an ADT for a node
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f"Node({self.value})"

# create an ADT for a binary search tree with add node(value), delete node(value), findnode(value), and printTree()
class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Add Node
    def add_node(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._add_recursive(self.root, value)

    def _add_recursive(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self._add_recursive(current.left, value)
        elif value > current.value:
            if current.right is None:
                current.right = Node(value)
            else:
                self._add_recursive(current.right, value)
        # If equal, do nothing (no duplicates in BST)

    # Find Node
    def find_node(self, value):
        return self._find_recursive(self.root, value)

    def _find_recursive(self, current, value):
        if current is None:
            return None
        elif value == current.value:
            return current
        elif value < current.value:
            return self._find_recursive(current.left, value)
        else:
            return self._find_recursive(current.right, value)

    # Delete Node
    def delete_node(self, value):
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, current, value):
        if current is None:
            return None

        # Traverse tree
        if value < current.value:
            current.left = self._delete_recursive(current.left, value)
        elif value > current.value:
            current.right = self._delete_recursive(current.right, value)
        else:
            # Found node to delete
            # Case 1: No child
            if current.left is None and current.right is None:
                return None
            # Case 2: One child
            elif current.left is None:
                return current.right
            elif current.right is None:
                return current.left
            # Case 3: Two children
            else:
                successor = self._find_min(current.right)
                current.value = successor.value
                current.right = self._delete_recursive(current.right, successor.value)

        return current

    def _find_min(self, node):
        while node.left is not None:
            node = node.left
        return node

    # Print Tree (In-order Traversal)
    def print_tree(self):
        def inorder(node):
            if node:
                inorder(node.left)
                print(node.value, end=" ")
                inorder(node.right)

        inorder(self.root)
        print()  # new line after print


# randomly generating an input set of size 5 to 50 for numbers between 1 and 1000
import random
def generate_random_input(size):
    return random.sample(range(1, 1001), size)

def main():
    bst = BinarySearchTree()
    size = random.randint(5, 50)
    random_values = generate_random_input(size)

    print("Random Values to Insert:", random_values)

    for value in random_values:
        bst.add_node(value)

    print("Initial BST (in-order traversal):")
    bst.print_tree()

    # Exercise add node
    new_value = random.randint(1, 1000)
    print(f"Adding Node with value {new_value}")
    bst.add_node(new_value)
    print("BST In-order Traversal after Addition:")
    bst.print_tree()

    # Exercise find_node - positive case
    test_value = random.choice(random_values)
    found_node = bst.find_node(test_value)
    print(f"Positive - Finding Node with value {test_value}:", found_node)

    # Exercise find_node - negative case
    # find a value between 1 and 1000 that is not in random_values
    while True:
        test_value = random.randint(1, 1000)
        if test_value not in random_values:
            break
    found_node = bst.find_node(test_value)
    print(f"Negative - Finding Node with value {test_value}:", found_node)

    # Test delete_node
    delete_value = random.choice(random_values)
    print(f"Deleting Node with value {delete_value}")
    bst.delete_node(delete_value)
    print("BST In-order Traversal after Deletion:")
    bst.print_tree()

if __name__ == "__main__":
    main()