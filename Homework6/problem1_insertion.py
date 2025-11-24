# Implement an insertion sort function
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Read input from file, sort it using insertion sort
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

    # perform insertion sort
    sorted_arr = insertion_sort(arr)
    print('Insertion sort result:', " ".join(map(str, sorted_arr)))

if __name__ == "__main__":
    main()

end_time = time.time()    # record end time
elapsed_time = end_time - start_time
print(f"Runtime: {elapsed_time:.6f} seconds")



