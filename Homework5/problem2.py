# Morse Code Vowel Problem
import sys

morse_vowel_list = ['.-', '.', '..', '---', '..-']


# Build a 3 by n matrix with 3 rows representing 1/2/3 characters to consider and n being the length of input

def vowel_calculation(input_code):
    n = len(input_code)
    matrix = [[0] * (n) for _ in range(3)]

    for i in range(n):
        row1 = input_code[i]
        row2 = input_code[i:i+2]
        row3 = input_code[i:i+3]

        # Check for the 1st character in the input string
        # The first character, base condition: look for 1, 2, and 3 characters ahead
        # If it is a vowel, mark it as 1
        if i == 0:
            if row1 in morse_vowel_list:
                matrix[0][i] = 1
            if row2 in morse_vowel_list:
                matrix[1][i] = 1
            if row3 in morse_vowel_list:
                matrix[2][i] = 1
        if i == 1:
            if row1 in morse_vowel_list:
                matrix[0][i] = matrix[0][i-1]
            if row2 in morse_vowel_list:
                matrix[1][i] = matrix[0][i-1]
            if row3 in morse_vowel_list:
                matrix[2][i] = matrix[0][i-1]
        if i == 2:
            if row1 in morse_vowel_list:
                matrix[0][i] = matrix[0][i-1] + matrix[1][i-2]
            if row2 in morse_vowel_list:
                matrix[1][i] = matrix[0][i-1] + matrix[1][i-2]
            if row3 in morse_vowel_list:
                matrix[2][i] = matrix[0][i-1] + matrix[1][i-2]
        if i >= 3:
            if row1 in morse_vowel_list:
                matrix[0][i] = matrix[0][i-1] + matrix[1][i-2] + matrix[2][i-3]
            if i <= n-2 and row2 in morse_vowel_list:
                matrix[1][i] = matrix[0][i-1] + matrix[1][i-2] + matrix[2][i-3]
            elif i > n-2:
                matrix[1][i] = ['X']
            if i <= n-3 and row3 in morse_vowel_list:
                matrix[2][i] = matrix[0][i-1] + matrix[1][i-2] + matrix[2][i-3]
            elif i > n-3:
                matrix[2][i] = ['X']
        
    return (matrix[0][n-1] + matrix[1][n-2] + matrix[2][n-3])

def main():

    # Read input from standard input
    input_lines = sys.stdin.read().strip().split("\n")
    
    # first line as n
    n = int(input_lines[0])
    # second line as the Morse code string
    morse_code = input_lines[1].strip()

    # Count vowels in the Morse code string
    result = vowel_calculation(morse_code)
    print('The Number of Vowel combinations is:', result)



if __name__ == "__main__":
    main()