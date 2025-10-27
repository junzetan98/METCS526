# Compute the smallest number of elements from the array whose sum is greater than the target T
# Use standard input to read the first line as n, the second line as the target T, 
# and the third line as the array of numbers (seperated by space)
import sys
def main():
    # Read the file from standard input 
    lines = sys.stdin.read().strip().split("\n")

    # Step 1: First line is n
    n = int(lines[0])
    # Step 2: Second line is target T
    T = int(lines[1])
    # Step 3: Third line is the array of numbers
    arr = list(map(int, lines[2].split()))

    # Print input and target
    print('Input:', arr)
    print('Target:', T)

    # Step 4: Sort the array in descending order to get the largest numbers first
    arr.sort(reverse=True)

    # Step 5: Initialize variables to keep track of the sum and count of elements
    current_sum = 0
    count = 0

    # Step 6: Iterate through the sorted array and accumulate the sum
    for num in arr:
        current_sum += num
        count += 1
        # Check if the current sum exceeds the target T
        if current_sum > T:
            print('Answer:', count)
            return
        
if __name__ == "__main__":
    main()