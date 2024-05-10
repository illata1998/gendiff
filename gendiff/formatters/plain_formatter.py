def convert_to_str(value):
    if isinstance(value, str):
        return f"'{value}'"
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, (list, dict, tuple)):
        return '[complex value]'
    else:
        return str(value)


def render_plain(diff_list, path=''):
    lines = []
    for item in diff_list:
        flag = item['flag']
        key = item['key']
        current_path = path + '.' + key if path else key
        match flag:
            case 'added':
                new_value = convert_to_str(item['new_value'])
                lines.append(f"Property '{current_path}' was {flag} "
                             f"with value: {new_value}")
            case 'removed':
                lines.append(f"Property '{current_path}' was {flag}")
            case 'updated':
                old_value = convert_to_str(item['old_value'])
                new_value = convert_to_str(item['new_value'])
                lines.append(f"Property '{current_path}' was {flag}. "
                             f"From {old_value} to {new_value}")
            case 'nested':
                lines.append(render_plain(item['children'], path=current_path))
            case 'same':
                continue
    return '\n'.join(lines)
