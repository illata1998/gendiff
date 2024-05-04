import json
import itertools


def stringify(value, replacer=' ', spaces_count=1):

    def iter_(current_value, depth):
        if not isinstance(current_value, dict):
            if isinstance(current_value, bool):
                return str(current_value).lower()
            return str(current_value)

        deep_indent_size = depth + spaces_count
        deep_indent = replacer * deep_indent_size
        current_indent = replacer * depth
        lines = []
        for key, val in current_value.items():
            lines.append(f'{deep_indent}{key}: {iter_(val, deep_indent_size)}')
        result = itertools.chain("{", lines, [current_indent + "}"])
        return '\n'.join(result)

    return iter_(value, 0)


def generate_diff(file_path1, file_path2):
    with open(file_path1) as file1, open(file_path2) as file2:
        data1 = json.load(file1)
        data2 = json.load(file2)
    result = {}
    for key in data1:
        if key in data2:
            if data1[key] == data2[key]:
                result['  ' + key] = data1[key]
            else:
                result['- ' + key] = data1[key]
                result['+ ' + key] = data2[key]
        else:
            result['- ' + key] = data1[key]
    for key in data2:
        if key not in data1:
            result['+ ' + key] = data2[key]
    result = dict(sorted(result.items(), key=lambda x: x[0][2:]))
    return stringify(result)
