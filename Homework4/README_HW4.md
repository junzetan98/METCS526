# METCS526 HW4

Problem 1: Nodes sequence for different traversal
Answer: 
    Preorder Traversal: ABEFHICDG
    Breadth-First (BFS): ABCDEFGHI
    Postorder Traversal: HEIFBCGDA
    In-Order Traversal: DGBEACHFI


Problem 2: Compute the smallest number of elements from the array whose sum is greater than the target T
Answer:
    The core of the algorithm is to compare the sum of the largest values with the target T number. It is like selecting the best members in a group to match with the target 'opponent'. The algorithm should return the number of 'best members' -- the largest numbers in the array -- which enable the sumed up number to exceed the target number. To do this, one has to first sort the list (from largest to smallest), and then loop through the list to find the count of numbers when the sum of numbers exceeds the target T. 
Test Case: 
    Screen Shot 'Screenshot HW4_Q2_fewest_1 & 2 Answer.png'
    Screen Shot 'Screenshot HW4_Q2_fewest_3 Answer.png'

Problem 3: Design an algorithm that determines the unique number of right triangles that can be formed by choosing sets of three points
Answer:
    The core of my algorithm is to find out all the cases where the dot product (x1*x2 + y1*y2) of two points in relation to the shifted origin is 0 (zero). In this case, the shifted origin is the unique right angle of the triangle formed by the 3 points in consideration. If the dot product of the two points in relation to the origin is 0, it means that the two lines formed by the two points with the origin become perpendicular, indicating a 90-degree angle at origin. To do this, my algorithm first shifts all points to the origin (O(n)), and for each origin, find the combination of every other 2 points and use the points' slopes with the origin to find perpendicular slopes (O(n^2)). This is a O(n^3) algorithm which runs within 60 seconds for the 3rd test case (1000 points).
Test Case:
    Screenshot HW4_Q3_answer1.png
    Screenshot HW4_Q3_answer2.png
    Screenshot HW4_Q3_answer3.png