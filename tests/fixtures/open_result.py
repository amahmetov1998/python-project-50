def open_file(filepath):
    with open(filepath, 'r') as file:
        return file.read()