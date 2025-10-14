# METCS526 HW3

Problem 1: Write a program to determine if a given string is a palindrome
Answer: 
    The core of this algorithm is to determine whether the given string is 'symmetric' in structure. To do this, a recursive function is used to check the first and last characters in the string, and then check the same case without the first and last characters of the 'previous' string (return is_palindrome(s[1:-1])), until the size of string needed to be tested reaches 0 or 1. 
Test Case (in command line):
    python HW3_Q1.py < palendrome_0.txt 'Screenshot Question 1_palendrome_0'
    python HW3_Q1.py < palendrome_1.txt 'Screenshot Question 1_palendrome_1'


Problem 2: Use recursion to create a function that prints and counts the unique sets of substrings of a given string
Answer:
    The core of this algorithm is to slice the string into substrings starting from the first character. The size of the slice should be 1, 1+1, 1+2, ..., n. Then, the process will be repeated excluding the initial character, until all the characters in the string have become the starting point once. The outcome (substrings) will then be put in a python set for retreiving and counting unique values.
Test Case: 
    Screen Shot 'Screenshot Question 2'

Problem 3: Use recursion and make a function to reverse a stack implemented as an array/linked-list/doubly-linked-list
Answer:
    The main logic for reversing a stack is to pop the stack top element and push it into another stack. This process will be recurred until the original stack becomes empty. This logic is applied in all three cases.
Test Case: 
    Screen Shot 'Screenshot Question 3_Reverse Array'
    Screen Shot 'Screenshot Question 3_Reverse Linked List'
    Screen Shot 'Screenshot Question 3_Reverse Doubly Linked List'

Problem 4: Create a solution to see if all ghosts can be eliminated in a single shot of ghostbusters
Answer:
    The core for this problem is to check whether the lines created by the ghostbuster-ghost pairs are all parellel or not. If all the lines are parellel, all ghosts were eliminated. The indicator for lines to be parellel is the slopes of the lines. If the slopes of all lines are the same, those lines are likely to be parellel. One edge case considered in my code is when lines have the same slopes but overlap (meaning that those are essentially the same line). Such cases will be judged to be 'All ghosts are NOT eliminated'. To check this, I also calculated the intercepts of lines, and decide that those lines are truly 'parellel to each others' when the number of unique values of intercepts equals n, the total number of pairs (meaning that those lines are different but parellel lines).
Test Case:
    python HW3_Q4.py < ghostbusters_input_7.txt (Returned: All Ghosts: were eliminated) 'Screenshot Question 4_input 7'
    python HW3_Q4.py < ghostbusters_input_8.txt (Returned: All Ghosts: were eliminated) 'Screenshot Question 4_input 8'
    python HW3_Q4.py < ghostbusters_input_3.txt (Returned: All Ghosts: were not eliminated) 'Screenshot Question 4_input 3'