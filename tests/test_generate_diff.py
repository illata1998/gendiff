from gendiff.modules.gendiff_func import generate_diff


def test_generate_diff():
    file_path1 = 'tests/fixtures/file1.json'
    file_path2 = 'tests/fixtures/file2.json'
    result_file1 = open('tests/fixtures/result1.txt')
    result_file2 = open('tests/fixtures/result2.txt')
    result1 = result_file1.read()[:-1]
    result2 = result_file2.read()[:-1]
    result_file1.close()
    result_file2.close()
    assert result1 == generate_diff(file_path1, file_path2)
    assert result2 == generate_diff(file_path1, file_path1)
