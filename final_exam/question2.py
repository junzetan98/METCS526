# Downhill Skier
import heapq
def longest_downhill(grid, count_matrix, max_positions):

    # Find the maximum value(s) in the grid and its positions
    if not max_positions: # if max_positions is empty, find the max value in the grid as initial step
        max_value = max(max(row) for row in grid)
        max_positions = [
        (i, j)
        for i, row in enumerate(grid)
        for j, v in enumerate(row)
        if v == max_value
        ]

    print('Max value:', max_value)
    print('Positions of max value:', max_positions)

    next_max = 0
    heap = [] # to store the next positions to explore
    for x, y in max_positions: # push all max positions into heap
        heapq.heappush(heap, (-grid[x][y], x, y)) # use negative value to create max-heap behavior

    for position in max_positions: # for each max position, start rolling downhill; here, evaluate the maximum path first; later, supplement that with 
        adjacent_directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (1,1), (-1,-1), (1,-1), (-1,1)] # down , up, left, right, and diagonals
        x, y = position
        current_value = grid[x][y]
        for direction in adjacent_directions:
            new_x, new_y = x + direction[0], y + direction[1]
            if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]):
                next_value = grid[new_x][new_y]
                if next_value < current_value:
                    count_matrix[new_x][new_y] = count_matrix[x][y] + 1 # update count matrix: if I can go downhill, add 1 to the path possibility
                    # record the downhill value positions and sort them from large to small

                    if next_value > next_max:
                        next_max = next_value
                        max_positions = [(new_x, new_y)]
                    elif next_value == next_max:
                        max_positions.append((new_x, new_y))

    print('Count matrix after first pass:', count_matrix)
    print('Next max value found:', next_max)
    print('New positions to explore:', max_positions)




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
    
    print('Grid:', grid)
    print('test: 1-0 value:', grid[1][0])
    longest_downhill(grid, count_matrix, max_positions=[])
    



if __name__ == "__main__":
    main()