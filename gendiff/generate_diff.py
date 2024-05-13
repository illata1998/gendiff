from gendiff.parser import parser
from gendiff.get_diff import get_diff
from gendiff.formatters.choose_formatter import choose_formatter
import os.path


def get_data_from_file(file_path):
    _, extension = os.path.splitext(file_path)
    with open(file_path) as file:
        return parser(file.read(), extension[1:])


def generate_diff(file_path1, file_path2, format_name='stylish'):
    data1 = get_data_from_file(file_path1)
    data2 = get_data_from_file(file_path2)
    formatter = choose_formatter(format_name)
    return formatter(get_diff(data1, data2))
