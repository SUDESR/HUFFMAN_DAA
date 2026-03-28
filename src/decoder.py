def decode(encoded_text, root):
    decoded_text = ""
    current = root

    for bit in encoded_text:
        if bit == '0':
            current = current.left
        else:
            current = current.right

        if current.char is not None:
            decoded_text += current.char
            current = root

    return decoded_text