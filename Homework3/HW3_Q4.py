# Create a solution to see if all ghosts can be eliminated in a single shot of ghostbusters

# Define a function that take in the ghostbusters test file and calculate the slopes of each pair
import sys

def main():
    # Read the file from standard input
    lines = sys.stdin.read().strip().split("\n")

    # Step 1: First line is n
    n = int(lines[0])

    # Prepare lists for the data
    xb_list, yb_list, xg_list, yg_list, slope_list, intercept_list = [], [], [], [], [], []

    # Step 2: Process each line
    for line in lines[1:]:
        parts = line.split()
        # B xb yb G xg yg
        xb = float(parts[1])
        yb = float(parts[2])
        xg = float(parts[4])
        yg = float(parts[5])
        
        # Append to lists
        xb_list.append(xb)
        yb_list.append(yb)
        xg_list.append(xg)
        yg_list.append(yg)

        # Step 3: Calculate slope
        if xb != xg:  # avoid division by zero
            slope = (yb - yg) / (xb - xg)
            intercept = yb - slope * xb
        else:
            slope = float('inf')  # vertical line
            intercept = xb  # x-intercept for vertical line
        slope_list.append(slope)
        intercept_list.append(intercept)
    
    # Test print the list for slopes
    # print("Slopes calculated:", slope_list)
    # print("Intercepts calculated:", intercept_list)

    # Step 4: Check if all slopes are the same AND if the number of unique intercepts is n (different lines)
    slope_check = len(set(slope_list)) # Use set to find unique slopes
    intercept_check = len(set(intercept_list)) # Use set to find unique intercepts
    # print('Number of unique intercepts:', intercept_check)
    # print("Number of pairs (n):", n)
    if slope_check == 1 and intercept_check == n:
        print("All Ghosts: were eliminated")
    else:
        print("All Ghosts: were not eliminated")



if __name__ == "__main__":
    main()