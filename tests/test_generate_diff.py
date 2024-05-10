from gendiff.modules.generate_diff import generate_diff


def test_generate_diff_flat():
    json_path1 = 'tests/fixtures/flat1.json'
    json_path2 = 'tests/fixtures/flat2.json'
    yaml_path1 = 'tests/fixtures/flat1.yaml'
    yaml_path2 = 'tests/fixtures/flat2.yml'
    with open('tests/fixtures/result_flat_stylish.txt') as result_stylish_file:
        result_stylish = result_stylish_file.read()[:-1]
    with open('tests/fixtures/result_flat_plain.txt') as result_plain_file:
        result_plain = result_plain_file.read()[:-1]
    with open('tests/fixtures/result_flat_json.txt') as result_json_file:
        result_json = result_json_file.read()[:-1]
    assert result_stylish == generate_diff(json_path1, json_path2)
    assert result_stylish == generate_diff(yaml_path1, yaml_path2)
    assert result_stylish == generate_diff(json_path1, yaml_path2)
    assert result_plain == generate_diff(json_path1, json_path2, 'plain')
    assert result_json == generate_diff(json_path1, json_path2, 'json')


def test_generate_diff_nested():
    json_path1 = 'tests/fixtures/nested1.json'
    json_path2 = 'tests/fixtures/nested2.json'
    yaml_path1 = 'tests/fixtures/nested1.yaml'
    yaml_path2 = 'tests/fixtures/nested2.yml'
    with open('tests/fixtures/result_nested_stylish.txt') as result_stylish_file:
        result_stylish = result_stylish_file.read()[:-1]
    with open('tests/fixtures/result_nested_plain.txt') as result_plain_file:
        result_plain = result_plain_file.read()[:-1]
    with open('tests/fixtures/result_nested_json.txt') as result_json_file:
        result_json = result_json_file.read()[:-1]
    assert result_stylish == generate_diff(json_path1, json_path2)
    assert result_stylish == generate_diff(yaml_path1, yaml_path2)
    assert result_stylish == generate_diff(json_path1, yaml_path2)
    assert result_plain == generate_diff(json_path1, json_path2, 'plain')
    assert result_json == generate_diff(json_path1, json_path2, 'json')
