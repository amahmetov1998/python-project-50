import pytest
from gendiff import generate_diff
from tests.fixtures.open_result import open_file


@pytest.mark.parametrize('file_1, file_2, expected',
                         [('gendiff/file1.json', 'gendiff/file2.json',
                           open_file('tests/fixtures/json_result'))])
def test_generate_diff(file_1, file_2, expected):
    assert generate_diff(file_1, file_2) == expected
