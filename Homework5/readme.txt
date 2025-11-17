Problem 1: Binary Search Tree Executions
Input: python problem1.py
Outputs: Screenshot HW5 problem1 - BST Executions
Explanations:
    Problem 1 asks about building a node class and a binary search tree class. To do this, a Node class
    with left and right sentinel nodes is created. Then to build the binary search tree (BST) class,
    a recursive add_node function, a recursive find_node function, and a recursive delete_node function
    are constructed to build the tree following the binary search tree principles. After building the BST
    ADT, I generated a set of random values from 1 to 1000 (with size between 5 and 50) using the random 
    package, and performed adding, finding value (with both positive and negative cases), and deleting 
    value operations on my binary search tree. 

Problem 2: Morse Code Vowels
Input: python problem2.py < vowel_input1.txt
       python problem2.py < vowel_input2.txt
       python problem2.py < vowel_input3.txt
       python problem2.py < vowel_input4.txt
Outputs: Screenshot HW5 problem2 - Vowels

Explanations:
    The heart of the algorithm is to find all the possible ways that a string containing all vowels can be formed from an input string of morse code.
    A vowel of morse code can be formed by 1/2/3 characters, so in my algorithm, I will track the 3 states of vowel combinations
    individually (represented by 3 rows in a table). This memorization algorithm works by keeping track of all the possible ways 
    that a vowel can be formed by each of the 3 states (i.e. by 1/2/3 input morse code).
    The initial condition to the algorithm says that in order to start, I must have a vowel: if a vowel can be made at the first
    position, put a 1, and do that for all states (e.g. if the input starts with a '.', then the vowel E can be made, then put a 1 at row 1 column 1);
    The algorithm then goes by checking if a vowel can be formed by looking ahead by n characters (with n = 1/2/3). If a vowel can be formed, look back by 
    n characters (with n=1/2/3); if no vowel can be made, put down a 0.
    When looking back, look back 1 position and check for state 1 (row 1), look back 2 positions and check down to state 2 (row 2), and look back 3 positions to check down to state 3 (row 3).
    If the places being checked have numbers - which represent the paths to get to that specific position - add those numbers together.
    This method essentially forms a diagonal, and this diagonal will be used for all states and characters going forward.
    If there is nothing in a diagonal, by definition it is a 0. If at row 2 and row 3, there is no enough space to check for the vowel (e.g. only 1 morse code left when checking for state 2),
    that place in the table will be made invalid (by putting in a 'X').
    The final answer for checking all the possible ways that can form a string containing all vowels is the last diagonal sum of the table. 



Problem 3: Longest alternating sequence
Input: 
    python problem3_copy.py < longest_seq1.txt
    python problem3_copy.py < longest_seq2.txt
    python problem3_copy.py < longest_seq3.txt
    python problem3_copy.py < longest_seq6.txt
    * The inputs for 4 and 5 won't finish.
Outputs: Screenshot HW5 problem3 - Sequences
Explanations:
    (Key: Run through all the combinations)
    This problem asks for the longest length of sequence X, where elements are chosen from sequence A and B following several
    selection rules (indice must be increasing, values must be increasing, two consecutive positions must be chosen from two different sequences).
    To takcle this, my algorithm checks for all the valid values in the alternating sequence, and if a valid value is found, recurse the process, 
    until either no valid values can be found or the end of either sequence is reached. A valid value here 
    is defined by: 
    (1) the value is located in the alternating sequence (if the previous value is in A, the current value must be in B);
    (2) the index of the next value must be larger than the index of previous value (if A[i] is chosen, the next value B[j] must follow j > i);
    (3) the value of the next value must be greater than the previous value (B[j] > A[i] with j > i).
    Because there can be multiple values that are in greater positions and are larger than the previous values,
    all the possible combinations for every value in both sequence A and sequence B will be checked, and the longest path for every value 
    will be recorded in the variable longest[0] (with longest being a list). Everytime a valid value is found, the counter variable
    'count' will be increased by 1, and if 'count' is greater than the current longest[0], longest[0] will become the value of 'count',
    so that the greatest 'count' value will be recorded and selected as the answer after all recursion processes end.
