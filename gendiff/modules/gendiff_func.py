from gendiff.modules.stringify_func import stringify
from gendiff.modules.parse_func import parse


def generate_diff(file_path1, file_path2):
    data1 = parse(file_path1)
    data2 = parse(file_path2)
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
