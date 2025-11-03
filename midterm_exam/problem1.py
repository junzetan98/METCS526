# Create an algorithm to determine if there exists three consecutive days 
# that produced more than half of the total snowfall across the n days

# read input from sys import stdin, read the first line as n and the second line
# as an array (sperated by space) of integers representing cumulative snowfall amounts for n days
import sys

def snowfall_exceeds_half(arr, n):
    total_snowfall = arr[-1]  # Total snowfall is the last element in cumulative array
    half_total = total_snowfall / 2

    # If there are exactly 3 days, the answer must be YES
    if n == 3:
        print('Solution: YES')
        return
    
    # If there are less than 3 days, the answer must be NO
    if n < 3:
        print('Solution: NO')
        return
    
    # If the 3rd day itself exceeds half the total snowfall compared to day 0 (0 snowfall),
    # the answer is YES
    if arr[2] - 0 > half_total:
        print('Solution: YES')
        return

    # Iterate through the array to check for three consecutive days
    for i in range(n - 3):
        # Snowfall in three consecutive days is arr[i+3] - arr[i]
        three_day_snowfall = arr[i + 3] - arr[i]
        if three_day_snowfall > half_total:
            print('Solution: YES')
            return
    print('Solution: NO')

def main():
    # Read the file from standard input 
    lines = sys.stdin.read().strip().split("\n")

    # Step 1: First line is n
    n = int(lines[0])
    # Step 2: Second line is the array of cumulative snowfall seperated by space
    arr = list(map(float, lines[1].split()))

    print('Input:', arr)

    snowfall_exceeds_half(arr, n)
    return




if __name__ == "__main__":
    main()

