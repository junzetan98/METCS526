Homework7_Huffman Encoding

Command line running:
    python encoding_copy.py < encoding_1.txt
    python encoding_copy.py < encoding_2.txt

Output Screenshots:
    Screenshot_Encoding_1_Code_Running.png
    Screenshot_Encoding_1_Output.png
    Screenshot_Encoding_2_Code_Running_Part1.png
    Screenshot_Encoding_2_Code_Running_Part2.png
    Screenshot_Encoding_2_Output.png

Explanations:
    The heart of the Huffman Encoding algorithm is to count the frequency of characters in the input, create a binary tree using 
    the frequencies of characters by merging the 2-lowest-frequency characters recursively, assign a Huffman code consisting of
    of 1 or 0 to each character based on the position of that character in the tree (i.e. 0 for left node and 1 for right node), 
    and use those binary codes to represent each character in the input data. To do that, the input texts will first be transformed
    to the binary number form using the Huffman codes. Then, for each 8 bytes (i.e. 8 1-or-0 characters), an ASCII character with the 
    same 1-and-0 combination will be chosen to become the encoded character for that 8-byte position. At the very end of the binary string,
    if there are less than 8 bytes left in the string, paddings of '1's will be added to the end of the string to make it ASCII character convertable.
    By using Huffman codes, we can shrink the total bytes of the input texts by merging and converting the original characters into encoded characters.

    To decode the encoded characters, we first turn the encoded ACSII characters back into binary strings, and remove any paddings. Then, we start from the first 
    number and refer back to the Huffman code to check whether we can get any match. If there is a match, we return that character and start again with the next
    character; if there is no match, we combine the next number and check again (i.e. for i in length(binary_string), check binary_string[:i+1] until there is a match).
    Because the Huffman binary tree will not produce a Huffman code with the same intermediate codes, the decoding process will not have the risk of mis-decoding.

    As for the implementation of Huffman Encoding, a min-heap is used for building the Huffman binary tree. A heap is helpful because it works as a priority queue where 
    the smallest number is always at the top of the queue. This enables us to get the 2 smallest values at each recursion and build our binary tree, as well as pushing the 
    newly merged item back into the priority queue to re-evaluate until there is only one element (the whole tree) remaining. In each recursion, the 2 smallest values will be 
    poped, and the left node (character with smaller frequency) will be recorded as '0' and the right node as '1'. This will generate our Huffman codes after all recursions.
    Then, a dictionary (huffman_dict) will be used to transform the codes into character - code pairs, and the dictionary will be used to produce the binary string for the input
    texts. The binary string will later be divided into 8-character chunks and be transformed into encoded ASCII characters, which is our encoded_output.txt file. That file will 
    then be used for decoding by referencing back to the Huffman codes created earlier. 