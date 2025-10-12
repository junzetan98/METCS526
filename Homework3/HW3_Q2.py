# Use recursion to create a function that 
# prints and counts the unique sets of substrings of a given string
import sys
def unique_substrings(s, substrings=None):
    if substrings is None:
        substrings = set() # Use set() to store unique substrings
    
    # Base case: if the string is empty, return the set of substrings
    # This is also the stopping condition for recursion
    if len(s) == 0:
        return substrings
    
    # Recursive case: generate all substrings starting from the first character
    for i in range(len(s)):
        substrings.add(s[:i+1])
    
    # Recur with the string excluding the first character
    return unique_substrings(s[1:], substrings)

# read input string from standard input and count total unique substrings
def main():
    string = input("Enter string: ").strip()
    substrings = unique_substrings(string)
    print(substrings)
    print("Total unique substrings:", len(substrings))

if __name__ == "__main__":
    main()