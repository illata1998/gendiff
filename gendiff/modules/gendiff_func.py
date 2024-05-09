from gendiff.modules.parse_func import parse
from gendiff.modules.diff import diff
from gendiff.modules.choose_formatter import choose_formatter


def generate_diff(file_path1, file_path2, format='stylish'):
    data1 = parse(file_path1)
    data2 = parse(file_path2)
    formatter = choose_formatter(format)
    return formatter(diff(data1, data2))

