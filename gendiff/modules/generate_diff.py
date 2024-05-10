from gendiff.modules.parse_files import parse_files
from gendiff.modules.get_diff import get_diff
from gendiff.formatters.choose_formatter import choose_formatter


def generate_diff(file_path1, file_path2, format_name='stylish'):
    data1 = parse_files(file_path1)
    data2 = parse_files(file_path2)
    formatter = choose_formatter(format_name)
    return formatter(get_diff(data1, data2))
