from gendiff.differ import build_diff
from gendiff.formatters.stylish import get_stylish
from gendiff.formatters.plain import get_plain
from gendiff.formatters.json import get_json
from gendiff.parser import parse


def read_file(filepath):
    with open(filepath) as f:
        return f.read()


def get_file_extension(filename):
    return filename[filename.find('.') + 1:]


def generate_diff(filepath_1, filepath_2, format='stylish'):
    read_file_1, read_file_2 = read_file(filepath_1), \
        read_file(filepath_2)
    extension_1, extension_2 = get_file_extension(filepath_1), \
        get_file_extension(filepath_2)
    parsed_file_1, parsed_file_2 = parse(read_file_1, extension_1), \
        parse(read_file_2, extension_2)
    diff_tree = build_diff(parsed_file_1, parsed_file_2)
    if format == 'plain':
        return get_plain(diff_tree)
    if format == 'json':
        return get_json(diff_tree)
    else:
        return get_stylish(diff_tree)
