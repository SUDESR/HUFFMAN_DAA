# Data Compression using Huffman Coding

##  Project Overview

This project implements **Huffman Coding**, a greedy algorithm used for **lossless data compression**. It reduces the size of data by assigning shorter binary codes to frequently occurring characters and longer codes to less frequent ones.

---

##  Objectives

* Implement Huffman Coding using DAA concepts
* Demonstrate greedy algorithm in practice
* Perform encoding and decoding of data
* Calculate compression ratio

---

## Concepts Used

* Greedy Algorithm
* Binary Tree
* Min Heap (Priority Queue)
* Prefix Codes

---

## Project Structure

```
Huffman_Project/
│
├── src/
│   ├── __init__.py
│   ├── huffman.py
│   ├── encoder.py
│   ├── decoder.py
│
├── utils/
│   ├── file_handler.py
│
├── data/
│   ├── input.txt
│   ├── compressed.txt
│   ├── output.txt
│
├── main.py
├── test_huffman.py
└── README.md
```

---

##  File Description

### 🔹 src/huffman.py

* Implements Huffman Tree construction
* Generates binary codes based on character frequency
* Contains optional function to print the tree

---

### 🔹 src/encoder.py

* Encodes input text into binary format using generated codes

---

### 🔹 src/decoder.py

* Decodes binary data back into original text using the Huffman tree

---

### 🔹 utils/file_handler.py

* Handles file input and output operations
* Reads input text and writes results to files

---

### 🔹 main.py

* Entry point of the project
* Coordinates all modules
* Executes full workflow from input to output

---

### 🔹 data/input.txt

* Stores input text to be compressed

---

### 🔹 data/compressed.txt

* Stores encoded binary data

---

### 🔹 data/output.txt

* Stores decoded text (same as input)

---

### 🔹 test_huffman.py

* Used for testing tree construction and code generation

---

##  How to Run

### Step 1: Add input

Open `data/input.txt` and enter your text.

Example:

```
data compression using huffman coding
```

---

### Step 2: Run the program

```
python main.py
```

---

##  Output

* Huffman codes displayed in terminal
* Encoded binary stored in `compressed.txt`
* Decoded text stored in `output.txt`
* Compression ratio printed

---

##  Compression Ratio

Compression ratio is calculated as:

```
Compression Ratio = Original Size (bits) / Compressed Size (bits)
```

* Original Size = Number of characters × 8
* Compressed Size = Length of encoded binary string

---

##  Example

**Input:**

```
aabbbc
```

**Encoded Output:**

```
111100010
```

**Decoded Output:**

```
aabbbc
```

---

##  Features

* Modular code structure
* File-based input and output
* Efficient encoding and decoding
* Compression ratio calculation
* Optional tree visualization

---

##  Limitations

* Huffman tree is not stored for reuse
* Decoding requires the same tree
* Binary data stored as string format

---

##  Future Enhancements

* Store Huffman tree for independent decoding
* Implement binary file compression
* Add graphical user interface
* Improve storage efficiency

---

##  Conclusion

This project demonstrates an efficient method for data compression using Huffman Coding. It highlights the use of greedy algorithms and tree-based structures in solving real-world problems.

---
