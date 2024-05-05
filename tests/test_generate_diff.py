from gendiff.modules.gendiff_func import generate_diff


def test_generate_diff():
    json_path1 = 'tests/fixtures/file1.json'
    json_path2 = 'tests/fixtures/file2.json'
    yaml_path1 = 'tests/fixtures/file1.yaml'
    yaml_path2 = 'tests/fixtures/file2.yml'
    result_file = open('tests/fixtures/result.txt')
    result = result_file.read()[:-1]
    result_file.close()
    assert result == generate_diff(json_path1, json_path2)
    assert result == generate_diff(yaml_path1, yaml_path2)
    assert result == generate_diff(json_path1, yaml_path2)
