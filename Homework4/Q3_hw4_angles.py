# Read the first line in the input text file as n, 
# and the following lines as the XY coordinates of a point
import sys
from itertools import combinations
import time

# Define a shift_origin function to shift the origin to a new point
def shift_origin(points, new_origin):
    shifted_points = []
    ox, oy = new_origin
    for (x, y) in points:
        shifted_points.append((x - ox, y - oy))
    return shifted_points

start_time = time.time()

def main():
    # Read the file from standard input 
    lines = sys.stdin.read().strip().split("\n")

    # Step 1: First line is n
    n = int(lines[0])

    if n < 3:
        print("The number of right triangles is: 0")
        return

    # Read the following lines as XY coordinates and store them in a list
    points = []
    # test2 = set()
    for line in lines[1:]:
        x, y = map(float,
                   line.split())
        points.append((x, y))
        # test2.add((x, y))

    # Test print the points list and number of points
    # print("Points:", points)
    # print("Number of points (n):", n)
    # test whether all points are unique
    # if len(test2) == n:
        # print("Points are unique.")
        # return

    # Step 2: For every point, shift the origin to that point 
    # and calculate the combinations of every other 2 points to check for right angles;
    # If any right angle is found, add 1 to the right_triangle counter
    count = 0
    #test = []
    for i in range(n):
        new_origin = points[i]
        shifted_points = shift_origin(points, new_origin)

        # Delist the origin point itself
        shifted_points.pop(i)

        # Take the combination of every other 2 points and calculate the dot product
        for (p1, p2) in combinations(shifted_points, 2):
        # Vectors from origin to points
            x1, y1 = p1
            x2, y2 = p2

            if x1 * x2 + y1 * y2 == 0:
                # print the 3 points that form a right triangle
                # print("Right triangle found with points:", new_origin,
                      # (x1 + new_origin[0], y1 + new_origin[1]),
                      # (x2 + new_origin[0], y2 + new_origin[1]))
                count += 1

                # record the 3-point set that forms a right triangle to a list and find duplicates
                # test.append(tuple(sorted([
                                # new_origin,
                                #(x1 + new_origin[0], y1 + new_origin[1]),
                                #(x2 + new_origin[0], y2 + new_origin[1])
                                #])))
                

    # find duplicates in test and print them
    # duplicates = [item for item in test if test.count(item) > 1]
    # print('Duplicate item:', duplicates)
    print("The number of right triangles is:", count)

    # Use pitagon theorem to verify the count
    # verified_count = 0
    # for triangle in test:
        #a = triangle[0]
        #b = triangle[1]
        #c = triangle[2]
        #ab2 = (a[0]-b[0])**2 + (a[1]-b[1])**2
        #ac2 = (a[0]-c[0])**2 + (a[1]-c[1])**2
        #bc2 = (b[0]-c[0])**2 + (b[1]-c[1])**2
        #sides = sorted([ab2, ac2, bc2])
        #if abs(sides[0] + sides[1] - sides[2]) < 1e-9:
        #    verified_count += 1
    #print("Verified number of right triangles using Pythagorean theorem:", verified_count)

if __name__ == "__main__":
    main()

end_time = time.time()    # record end time
elapsed_time = end_time - start_time
print(f"Runtime: {elapsed_time:.6f} seconds")