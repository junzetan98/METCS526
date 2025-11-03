# Pandemic - judge whether the pandemic will stop
from collections import Counter
import sys

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Create a recursive function to determine the list of infected individuals
# and check whether all points in the n x n grid are infected
def infected_check(list, n):
    # take the stdin input and put all the infected individuals in a list
    
    # Edge case check 1: if there are 2 or less infected points, there are healthy counties left
    if len(list) <= 2:
        print('There are healthy counties left')
        return
    
    

    all_adjacents = []  # store all neighbors for all infected points
    len_before = len(list)

    for x,y in list:
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            # Keep only points within the bounds 0 <= nx <= n-1 and 0 <= ny <= n-1
            if 0 <= nx <= n-1 and 0 <= ny <= n-1:
                all_adjacents.append((nx, ny))

    # Count occurrences of each point
    counts = Counter(all_adjacents)

    duplicates = [point for point, count in counts.items() if count > 1]

    # Append duplicates back to the original infected list (if not already present)
    for point in duplicates:
        if point not in list:
            list.append(point)
    
    # Check if new infections were added
    len_after = len(list)
    if len_after == len_before and len_after < n * n:
        # print(len_after)
        print('There are healthy counties left')
        return
    
    if len(list) == n * n:
        # print(len_after)
        print('There are no healthy counties left')
        return
    else:
        infected_check(list, n)


def main():
    # Read the file from standard input 
    lines = sys.stdin.read().strip().split("\n")

    # fist line as n
    n = int(lines[0])
    # for each of the following lines, read as (x, y) coordinates of infected individuals
    infected = []
    for line in lines[1:]:
        x, y = map(int, line.split())
        infected.append((x, y))

    # print('Input n:', n)    
    # print('Input Infected:', infected)

    infected_check(infected, n)


if __name__ == "__main__":
    main()