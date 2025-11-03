# Symbol Puzzle Game 

# Read the input from standard input
import sys

def spg_validate(input_grid, n):
    # first, check row uniqueness: each row must contain each symbol in the symbols list at 
    # most once, except for '.'; return 'The board is invalid' if any row have duplicate symbols values
    for row in input_grid:
        filtered = [s for s in row if s != '.']  # ignore '.'
        if len(filtered) != len(set(filtered)):  # check duplicates
            return 'The board is invalid'
    
    # second, check column uniqueness: each column must contain each symbol in the symbols list at 
    # most once, except for '.'; return 'The board is invalid' if any column have duplicate symbols values
    for col in range(n):
        col_values = [input_grid[row][col] for row in range(n)]
        filtered = [s for s in col_values if s != '.']  # ignore '.'
        if len(filtered) != len(set(filtered)):  # check duplicates
            return 'The board is invalid'
        
    # third, check sub-grid uniqueness: each sub-grid (size square root of n) must contain each symbol in the symbols list at 
    # most once, except for '.';
    subgrid_size = int(n**0.5)

    for start_row in range(subgrid_size):
        for start_col in range(subgrid_size):
            box_values = []
            for i in range(subgrid_size):
                for j in range(subgrid_size):
                    row = start_row * subgrid_size + i
                    col = start_col * subgrid_size + j
                    box_values.append(input_grid[row][col])
            filtered = [s for s in box_values if s != '.']  # ignore '.'
            if len(filtered) != len(set(filtered)):  # check duplicates
                return 'The board is invalid'
    
    # If all checks passed, the board is valid
    return 'The board is valid'


def main():
    lines = sys.stdin.read().strip().split("\n")
    # first line as n
    n = int(lines[0])
    # second line as the n-symbol list
    symbols = lines[1].split(",")
    # third line and below read as a 2D grid
    input_grid = [line.split(",") for line in lines[2:]]

    # print("Number of Symbols:", n)
    # print("Symbol List:", symbols)
    # print('Grid:', grid)
    # print('Grid Rows:', len(grid))

    result = spg_validate(input_grid, n)
    print(result)


if __name__ == "__main__":
    main()


    