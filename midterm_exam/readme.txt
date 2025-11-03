# METCS526 Midterm Exam Answers

Problem 1 (Screenshot_Problem1_input 1,2,3,4.png & Screenshot_Problem1_input 5,6.png, 
example input: python problem1.py < snowfall_input1.txt):

The heart of my algorithm is to compute the amount of snowfall for every consecutive three days 
in the array, and compare every amount of 3-day snowfall with the target (i.e. half of total 
n-day snowfall). If any 3-day snowfall amount is larger than the target, the solution will be 
YES.

For edge cases:

- if there are a total of less than 3 days, the solution must be NO;

- if there are exactly 3 days, the solution must be YES;

- if in the third day of the array, the snowfall amount already exceeds the target, 
the solution must be YES (since the snowfall of day 0 must be 0).

Problem 2 (Screenshot_Problem2, example input: python problem2.py < pandemic_input1.txt):

The heart of my algorithm for this problem is to recursively compute and record the unique 
counties to be infected by the pandemic (i.e. counties that have 2 or more neighbors), and 
compare the total number of counties infected before and after one recursion. The newly infected 
counties will be calculated as the duplicate neighor for more than 2 infected counties (by using 
a counter function).If the total infected counties reach the number of total counties, the 
solution will be 'there are no healthy counties left'. If the infected counties stop to increase 
and the total number of infected counties does not reach the total counties, the solution will
 be 'there are healthy counties left'.

Problem 3 (Screenshot_Problem3):

The heart of this algorithm is to recursively check the maximum numbers of items that can 
be purchased, starting from the left of the category list. Then, ignore the first left category 
and try finding the maximum number again from the second left category. The stopping condition 
for one recursion will be that unique categories being taken reach 3. After getting all the 
maximum numbers going through all the starting points, the biggest number is determined as 
the final solution of items being selected. 

The core aspect of my code is that I define a max_items(input_list) function and keep 
appending items from the input category list to the item list until the item list has more
than 2 unique categories. Once this condition is reached, the lastly added item will be 
removed and the length of the item list will be recorded to the max_number list. Then, 
the max_items() function will be called again without the first element in the previous 
input category list (i.e. max_items(input_list[1:])). After the input_list being examined 
becomes an empty list (meaning that all the starting points have been tested), the maximum 
number from the max_number list will be determined as the solution. 

Problem 4 (Screenshot_Problem4, example input: python problem4.py < spg_input1.txt):

The core of this algorithm is to (1) go through each row of the board (or grid/matrix) and 
check whether there are duplicated values; (2) go through each column of the board and check 
whether there are duplicated values; (3) divide the whole board into n sub-boards, and check 
whether there are duplicated values in each sub-board. If no duplicated values are found in all 
the three tests, the solution will be 'The board is valid'. Otherwise, the board will be invalid. 
Specifically in test (3), the number of sub-board will be determined as n (e.g. for a 4-by-4 board, 
there will be 4 2-by-2 sub-board, namely the top-left, top-right, bottom-left, and bottom-right 
ones, instead of 9 sub-boards in total). 

For the code, in test(1), each row in the board will be seperatly examined without considering 
the '.' symbol because a '.' will represent an empty space. If the length of the filtered list 
(i.e. a list of symbols without the '.' symbol) is different from the filtered list treated as a 
set(), it means that there are duplicated values in that row, and the board will be said to be 
invalid. The same logic applys to test(2), the column test. For test(3), each sub-board will 
first be found by dividing the whole board into n parts (4 sub-boards for a 4-by-4 board and 
9 sub-boards for a 9-by-9 board). Each element of the sub-boards will be appended to a box_value 
list, which will again be tested uniqueness. If no duplicated values are found in filtered lists 
in all 3 tests, the board will be treated as a valid board. 


