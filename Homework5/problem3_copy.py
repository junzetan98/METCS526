# longest sequence of alternating increasing values
import sys


def find_alternate(matrix, current_value, current_index, current_list, count, longest):
    if count > longest[0]:
        longest[0] = count
    
    if current_index == max(len(matrix[0]), len(matrix[1])) - 1:
        return # print('longest sequence: ', longest[0])
    
    other_list = 1 if current_list == 0 else 0
    
    # print('New iteration')
    found_any = False
    for i, value in enumerate(matrix[other_list][current_index+1:], current_index+1):
        if value > current_value:
            found_any = True
            # print(f'Found value {value} > {current_value} at index {i}')
            find_alternate(matrix, value, i, other_list, count + 1, longest)
    
    # If no valid values found, update longest with current count
    # if not found_any:
        # return print(longest)



def main():
    # Read input from standard input
    input_lines = sys.stdin.read().strip().split("\n")
    
    # first line as size_a
    size_a = int(input_lines[0])
    # second line as size_b
    size_b = int(input_lines[1])
    # third line as array a
    a = list(map(int, input_lines[2].split()))
    # fourth line as array b
    b = list(map(int, input_lines[3].split()))

    matrix = [a, b]
    longest = [0]

    # start with array a (row 0 in matrix)
    # find_alternate(matrix, 2, 1, 0, 1, longest)
    for item in matrix[0]:
        current_value = item
        current_index = matrix[0].index(item)
        current_list = 0
        count = 1
        find_alternate(matrix, current_value, current_index, current_list, count, longest)

    for item in matrix[1]:
        current_value = item
        current_index = matrix[1].index(item)
        current_list = 1
        count = 1
        find_alternate(matrix, current_value, current_index, current_list, count, longest)
    

    print('Longest Sequence: ', longest[0])

if __name__ == "__main__":
    main()
