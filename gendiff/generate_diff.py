from gendiff.get_diff import make_diff
from gendiff.formatters.stylish_format import get_stylish
from gendiff.formatters.plain_format import get_plain
from gendiff.formatters.json_format import get_json

from gendiff.open_file import open_file
from gendiff.parse_file import parse_file
from gendiff.get_file_extension import get_file_extension


def generate_diff(file_1, file_2, file_format='stylish'):
    opened_file_1, opened_file_2 = open_file(file_1), \
        open_file(file_2)
    extension_1, extension_2 = get_file_extension(file_1), \
        get_file_extension(file_2)
    parsed_file_1, parsed_file_2 = parse_file(opened_file_1, extension_1), \
        parse_file(opened_file_2, extension_2)
    diff_tree = make_diff(parsed_file_1, parsed_file_2)
    if file_format == 'plain':
        return get_plain(diff_tree)
    if file_format == 'json':
        return get_json(diff_tree)
    else:
        return get_stylish(diff_tree)
