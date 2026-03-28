def encode(text, codes):
    encoded_text = ""
    for char in text:
        encoded_text += codes[char]
    return encoded_text