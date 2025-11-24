# Implement a merge sort function
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    sorted_array = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            sorted_array.append(left[left_index])
            left_index += 1
        else:
            sorted_array.append(right[right_index])
            right_index += 1

    # Append any remaining elements from the left or right array
    sorted_array.extend(left[left_index:])
    sorted_array.extend(right[right_index:])

    return sorted_array

# Read input from file, sort it using merge sort
import sys

# keep track of running time
import time
start_time = time.time()



def main():
    # read file from standard input
    input_lines = sys.stdin.read().strip().split("\n")
    n = int(input_lines[0])
    arr = list(map(int, input_lines[1].split()))

    # print the input array
    print("Input array:", " ".join(map(str, arr)))

    # perform merge sort
    sorted_arr = merge_sort(arr)
    print('Merge sort result:', " ".join(map(str, sorted_arr)))

if __name__ == "__main__":
    main()

end_time = time.time()    # record end time
elapsed_time = end_time - start_time
print(f"Runtime: {elapsed_time:.6f} seconds")