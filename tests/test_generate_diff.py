from gendiff.modules.gendiff_func import generate_diff


def test_generate_diff():
    file_path1 = 'fixtures/file1.json'
    file_path2 = 'fixtures/file2.json'
    file_path3 = 'fixtures/file3.json'
    result_file1 = open('fixtures/result1.txt')
    result_file2 = open('fixtures/result2.txt')
    result_file3 = open('fixtures/result3.txt')
    result1 = result_file1.read()
    result2 = result_file2.read()
    result3 = result_file3.read()
    result_file1.close()
    result_file2.close()
    result_file3.close()
    assert result1 = generate_diff(file_path1, file_path2)
    assert result2 = generate_diff(file_path1, file_path1)
    assert result3 = generate_diff(file_path1, file_path3)
