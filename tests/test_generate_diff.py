import pytest
from gendiff.generate_diff import generate_diff


def read_results(result_path):
    with open(result_path) as result_file:
        return result_file.read()[:-1]


@pytest.mark.parametrize("result_path,formatter", [('tests/fixtures/result_flat_stylish.txt', 'stylish'),
                                                   ('tests/fixtures/result_flat_plain.txt', 'plain'),
                                                   ('tests/fixtures/result_flat_json.txt', 'json')])
@pytest.mark.parametrize("file_path1", ['tests/fixtures/flat1.json', 'tests/fixtures/flat1.yaml'])
@pytest.mark.parametrize("file_path2", ['tests/fixtures/flat2.json', 'tests/fixtures/flat2.yml'])
def test_generate_diff_flat(result_path, file_path1, file_path2, formatter):
    assert read_results(result_path) == generate_diff(file_path1, file_path2, format_name=formatter)


@pytest.mark.parametrize("result_path,formatter", [('tests/fixtures/result_nested_stylish.txt', 'stylish'),
                                                   ('tests/fixtures/result_nested_plain.txt', 'plain'),
                                                   ('tests/fixtures/result_nested_json.txt', 'json')])
@pytest.mark.parametrize("file_path1", ['tests/fixtures/nested1.json', 'tests/fixtures/nested1.yaml'])
@pytest.mark.parametrize("file_path2", ['tests/fixtures/nested2.json', 'tests/fixtures/nested2.yml'])
def test_generate_diff_nested(result_path, file_path1, file_path2, formatter):
    assert read_results(result_path) == generate_diff(file_path1, file_path2, format_name=formatter)
