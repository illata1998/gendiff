from gendiff.modules.gendiff_func import generate_diff


def test_generate_diff_flat():
    json_path1 = 'tests/fixtures/flat1.json'
    json_path2 = 'tests/fixtures/flat2.json'
    yaml_path1 = 'tests/fixtures/flat1.yaml'
    yaml_path2 = 'tests/fixtures/flat2.yml'
    result_file1 = open('tests/fixtures/result_flat.txt')
    result1 = result_file1.read()[:-1]
    result_file1.close()
    assert result1 == generate_diff(json_path1, json_path2)
    assert result1 == generate_diff(yaml_path1, yaml_path2)
    assert result1 == generate_diff(json_path1, yaml_path2)


def test_generate_diff_nested():
    json_path1 = 'tests/fixtures/nested1.json'
    json_path2 = 'tests/fixtures/nested2.json'
    yaml_path1 = 'tests/fixtures/nested1.yaml'
    yaml_path2 = 'tests/fixtures/nested2.yml'
    result_file1 = open('tests/fixtures/result_nested.txt')
    result1 = result_file1.read()[:-1]
    result_file1.close()
    assert result1 == generate_diff(json_path1, json_path2)
    assert result1 == generate_diff(yaml_path1, yaml_path2)
    assert result1 == generate_diff(json_path1, yaml_path2)
