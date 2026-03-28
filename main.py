from src.huffman import build_huffman_tree, generate_codes
from src.huffman import build_huffman_tree, generate_codes, print_tree
from src.encoder import encode
from src.decoder import decode
from utils.file_handler import read_file, write_file


def calculate_compression_ratio(original_text, encoded_text):
    original_bits = len(original_text) * 8
    compressed_bits = len(encoded_text)

    if compressed_bits == 0:
        return 0

    return original_bits / compressed_bits


def main():
    print("---- HUFFMAN CODING PROJECT ----")

    # Step 1: Read input
    text = read_file("data/input.txt")

    if not text:
        print("Input file is empty!")
        return

    print("\nOriginal Text:")
    print(text)

    # Step 2: Build Huffman Tree
    root = build_huffman_tree(text)
    print("\nHuffman Tree:")
    print_tree(root)

    # Step 3: Generate Codes
    codes = generate_codes(root)

    print("\nHuffman Codes:")
    for char, code in codes.items():
        print(f"{repr(char)} : {code}")

    # Step 4: Encode
    encoded_text = encode(text, codes)

    # Step 5: Save compressed
    write_file("data/compressed.txt", encoded_text)

    print("\nEncoded Text:")
    print(encoded_text)

    # Step 6: Decode
    decoded_text = decode(encoded_text, root)

    # Step 7: Save output
    write_file("data/output.txt", decoded_text)

    print("\nDecoded Text:")
    print(decoded_text)

    # Step 8: Compression Ratio
    ratio = calculate_compression_ratio(text, encoded_text)

    print(f"\nCompression Ratio: {ratio:.2f}")


if __name__ == "__main__":
    main()