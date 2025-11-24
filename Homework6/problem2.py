# Implement a Radix Sort
def counting_sort_for_radix(arr, exp):
    n = len(arr)
    output = [0] * n  # output array
    count = [0] * 10  # count array for digits (0 to 9)

    # Store count of occurrences in count[]
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # Change count[i] so that it now contains actual
    # position of this digit in output[]
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    # Copy the output array to arr[], so that arr[] now
    # contains sorted numbers according to the current digit
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    # Find the maximum number to know number of digits
    max1 = max(arr)

    # Do counting sort for every digit. exp is 10^i
    # where i is current digit number
    exp = 1
    while max1 // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10

# Read input from file, sort it using radix sort
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

    # perform radix sort
    radix_sort(arr)
    print('Radix sort result:', " ".join(map(str, arr)))

if __name__ == "__main__":
    main()

end_time = time.time()    # record end time 
elapsed_time = end_time - start_time
print(f"Runtime: {elapsed_time:.6f} seconds")


