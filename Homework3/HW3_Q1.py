# Determine if a given input string is a palindrome.
# take standard input txt file as input

import sys

# function to check if a string is a palindrome
def is_palindrome(s):
    # check base case: return true if the string is empty or has one character
    if len(s) <= 1:
        return True
    # check first and last characters: if they are not the same, return false
    if s[0] != s[-1]:
        return False
    # recursive case: check the substring without the first and last characters
    return is_palindrome(s[1:-1])

# read input from standard input, process each line, and count total palindromes
def main():
    count = 0
    for line in sys.stdin:
        line = line.strip()
        result = is_palindrome(line)
        print(result)
        if result:
            count += 1
    print("Total palindromes:", count)

if __name__ == "__main__":
    main()