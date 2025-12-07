# Huffman Encoding

def huffman_encoding_ascii(data):
    # Build frequency dictionary
    frequency = {}
    for char in data:
        frequency[char] = frequency.get(char, 0) + 1

    print("Character Frequencies:", frequency)

    # Create priority queue
    import heapq
    heap = [[weight, [char, ""]] for char, weight in frequency.items()]
    heapq.heapify(heap)

    # Build Huffman tree
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = "0" + pair[1]
        for pair in hi[1:]:
            pair[1] = "1" + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

    print("Huffman Tree:", heap)

    # Final mapping of characters to codes
    huffman_list = heapq.heappop(heap)[1:]
    huffman_dict = {char: code for char, code in huffman_list}

    # Encode the data and produce the bitstring -- waiting to be coverted to ASCII characters
    bitstring = ''.join(huffman_dict[ch] for ch in data)

    # --- Convert bitstring → ASCII ---

    # Pad to a multiple of 8 bits
    padding = (8 - len(bitstring) % 8) % 8
    bitstring += "1" * padding

    ascii_encoded = ""
    for i in range(0, len(bitstring), 8):
        byte = bitstring[i:i+8]           # 8-bit chunk
        ascii_encoded += chr(int(byte, 2))  # Convert to ASCII

    return ascii_encoded, huffman_dict, padding

def huffman_decoding_ascii(ascii_encoded, huffman_dict, padding):
    # --- Convert ASCII → bitstring ---
    bitstring = ""
    for char in ascii_encoded:
        byte = bin(ord(char))[2:].rjust(8, '0')  # Convert to 8-bit binary
        bitstring += byte

    # Remove padding
    if padding > 0:
        bitstring = bitstring[:-padding]

    # Reverse mapping
    reverse_dict = {v: k for k, v in huffman_dict.items()}

    # Decode the bitstring
    current_code = ""
    decoded_output = []

    for bit in bitstring:
        current_code += bit
        if current_code in reverse_dict:
            decoded_output.append(reverse_dict[current_code])
            current_code = ""

    return "".join(decoded_output)

def main():
    # Read input from file
    import sys

    # Read data from standard input
    input_data = sys.stdin.read().strip()

    print("Input data:", input_data)

    # Perform Huffman encoding
    encoded_data, huffman_codes, padding = huffman_encoding_ascii(input_data)
    print("Encoded data (ASCII):", encoded_data)
    print("Huffman Codes:", huffman_codes)

    # Write encoded data and codes to files
    with open("encoded_output.txt", "w", encoding="utf-8") as f:
        f.write(encoded_data)

    print('Encoded data written to "encoded_output.txt"')


    # Perform Huffman decoding
    decoded_data = huffman_decoding_ascii(encoded_data, huffman_codes, padding)
    print("Decoded data:", decoded_data)

if __name__ == "__main__":
    main()


    
