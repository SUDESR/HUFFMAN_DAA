from huffman import build_huffman_tree, generate_codes

# Test input
text = "aabbbc"

print("Input:", text)

# Step 1: Build tree
root = build_huffman_tree(text)

# Step 2: Generate codes
codes = generate_codes(root)

print("\nGenerated Huffman Codes:")
for char, code in codes.items():
    print(f"{char} : {code}")