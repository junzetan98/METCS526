# Downhill Skier
def longest_downhill(grid, count_matrix):
    # Create a dictionary to map values to their positions
    value_positions = {}

    for r, row in enumerate(grid):
        for c, value in enumerate(row):
            # If value is not in dictionary yet, create empty list
            if value not in value_positions:
                value_positions[value] = []

            # Append the current position (row, col)
            value_positions[value].append((r, c))

    # Sort this dictionary's keys in descending order to process from highest to lowest
    sorted_dict = dict(sorted(value_positions.items(), key=lambda x: x[0], reverse=True))
    # print('sorted_dict:', sorted_dict)

    for key in sorted(sorted_dict, reverse=True):
        start_positions = sorted_dict[key]

        for position in start_positions:
            adjacent_directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (1,1), (-1,-1), (1,-1), (-1,1)] # down , up, left, right, and diagonals
            x, y = position
            current_value = grid[x][y]
            for direction in adjacent_directions:
                new_x, new_y = x + direction[0], y + direction[1]
                if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]):
                    next_value = grid[new_x][new_y]
                    if next_value < current_value:
                        # update count matrix: if there is a way to go downhill, compare count+1 with existing count and keep the larger one
                        count_matrix[new_x][new_y] = max(count_matrix[new_x][new_y], count_matrix[x][y] + 1) 
    
    # After processing all positions, retrieve the maximum value from the count matrix
    max_path_length = max(max(row) for row in count_matrix)
    print('Longest Path:', max_path_length)



import sys
def main():
    # standard input reading
    input_data = sys.stdin.read().strip().splitlines()
    # read the first line as the row of the grid
    row = int(input_data[0])
    # second row as column number
    column = int(input_data[1])
    # from the 3rd line onwards, read the row by column grid (read each line as a list)
    grid = []
    for line in input_data[2:]:
        input = list(map(int, line.split()))
        grid.append(input)

    count_matrix = [[0 for _ in range(column)] for _ in range(row)]
    
    longest_downhill(grid, count_matrix)
    



if __name__ == "__main__":
    main()