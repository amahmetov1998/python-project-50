import pytest
from gendiff import generate_diff
from gendiff.open import open_file

plain_json_file_1 = 'tests/fixtures/plain_file1.json'
plain_json_file_2 = 'tests/fixtures/plain_file2.json'
plain_yaml_file_1 = 'tests/fixtures/plain_file1.yaml'
plain_yaml_file_2 = 'tests/fixtures/plain_file2.yaml'
nested_json_file_1 = 'tests/fixtures/nested_file1.json'
nested_json_file_2 = 'tests/fixtures/nested_file2.json'
nested_yaml_file_1 = 'tests/fixtures/nested_file1.yaml'
nested_yaml_file_2 = 'tests/fixtures/nested_file2.yaml'


@pytest.mark.parametrize('file_1, file_2, format, expected',
                         [(plain_json_file_1, plain_json_file_2, 'stylish',
                           open_file('tests/fixtures/plain_json_result')),
                          (plain_yaml_file_1, plain_yaml_file_2, 'stylish',
                           open_file('tests/fixtures/plain_yaml_result')),
                          (nested_json_file_1, nested_json_file_2, 'stylish',
                           open_file('tests/fixtures/nested_json_result')),
                          (nested_yaml_file_1, nested_yaml_file_2, 'stylish',
                           open_file('tests/fixtures/nested_json_result')),
                          (nested_json_file_1, nested_json_file_2, 'plain',
                           open_file('tests/fixtures/plain_result')),
                          (nested_json_file_1, nested_json_file_2, 'json',
                           open_file('tests/fixtures/json_result'))
                          ])
def test_generate_diff(file_1, file_2, format, expected):
    assert generate_diff(file_1, file_2, format) == expected
