from gendiff.get_diff import make_diff
from gendiff.formatters.stylish_format import get_stylish
from gendiff.formatters.plain_format import get_plain
from gendiff.formatters.json_format import get_json


def generate_diff(file_1, file_2, file_format='stylish'):
    diff_tree = make_diff(file_1, file_2)
    if file_format == 'plain':
        return get_plain(diff_tree)
    if file_format == 'json':
        return get_json(diff_tree)
    else:
        return get_stylish(diff_tree)
