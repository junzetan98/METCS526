# Shopping Cart Problem

# Define a function to recursively check the maximum items
# that can be added to the cart without exceeding 2 categories
import sys

max_number_list = []

def max_items(input_list):
    if not input_list:
        return

    item_list = []
    
    for item in input_list:
        item_list.append(item)
        if len(set(item_list)) > 2:
            item_list.pop()  # remove the last added item
            break  # stop when there are more than 2 unique items

    max_number_list.append(len(item_list))

    return max_items(input_list[1:])

def main():
    lines = sys.stdin.read().strip().split("\n")
    n = int(lines[0])
    # read line 2 as the list of items which are seperated by comma
    categories = lines[1].split(",")

    print('Input Categories:', categories)

    max_items(categories)

    print(max(max_number_list), 'items were selected')


if __name__ == "__main__":
    main()


            
    
    