import pytest
from gendiff import generate_diff
from gendiff.open_file import open_file
from gendiff.parse_file import parse_file
from gendiff.get_file_extension import get_file_extension
plain_json_file_1 = 'gendiff/files/plain_file1.json'
plain_json_file_2 = 'gendiff/files/plain_file2.json'
plain_yaml_file_1 = 'gendiff/files/plain_file1.yaml'
plain_yaml_file_2 = 'gendiff/files/plain_file2.yaml'
nested_json_file_1 = 'gendiff/files/nested_file1.json'
nested_json_file_2 = 'gendiff/files/nested_file2.json'
nested_yaml_file_1 = 'gendiff/files/nested_file1.yaml'
nested_yaml_file_2 = 'gendiff/files/nested_file2.yaml'


@pytest.mark.parametrize('file_1, file_2, format, expected',
                         [(parse_file(open_file(plain_json_file_1), get_file_extension(plain_json_file_1)),
                           parse_file(open_file(plain_json_file_2), get_file_extension(plain_json_file_2)), 'stylish',
                           open_file('tests/fixtures/plain_json_result')),
                          (parse_file(open_file(plain_yaml_file_1), get_file_extension(plain_yaml_file_1)),
                           parse_file(open_file(plain_yaml_file_2), get_file_extension(plain_yaml_file_2)), 'stylish',
                           open_file('tests/fixtures/plain_yaml_result')),
                          (parse_file(open_file(nested_json_file_1), get_file_extension(nested_json_file_1)),
                           parse_file(open_file(nested_json_file_2), get_file_extension(nested_json_file_2)), 'stylish',
                           open_file('tests/fixtures/nested_json_result')),
                          (parse_file(open_file(nested_yaml_file_1), get_file_extension(nested_yaml_file_1)),
                           parse_file(open_file(nested_yaml_file_2), get_file_extension(nested_yaml_file_2)), 'stylish',
                           open_file('tests/fixtures/nested_json_result')),
                          (parse_file(open_file(nested_json_file_1), get_file_extension(nested_json_file_1)),
                           parse_file(open_file(nested_json_file_2), get_file_extension(nested_json_file_2)), 'plain',
                           open_file('tests/fixtures/plain_result')),
                          (parse_file(open_file(nested_json_file_1), get_file_extension(nested_json_file_1)),
                           parse_file(open_file(nested_json_file_2), get_file_extension(nested_json_file_2)), 'json',
                           open_file('tests/fixtures/json_result'))
                          ])
def test_generate_diff(file_1, file_2, format, expected):
    assert generate_diff(file_1, file_2, format) == expected

