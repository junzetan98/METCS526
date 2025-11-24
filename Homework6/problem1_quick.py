# Implement a quick sort function
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

# Read input from file, sort it using quick sort
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

    # perform quick sort
    sorted_arr = quick_sort(arr)
    print('Quick sort result:', " ".join(map(str, sorted_arr)))

if __name__ == "__main__":
    main()

end_time = time.time()    # record end time
elapsed_time = end_time - start_time
print(f"Runtime: {elapsed_time:.6f} seconds")



