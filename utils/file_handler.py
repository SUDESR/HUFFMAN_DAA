def read_file(path):
    try:
        with open(path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print("File not found!")
        return ""


def write_file(path, data):
    with open(path, 'w') as file:
        file.write(data)