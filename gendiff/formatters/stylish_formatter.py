from itertools import chain


def convert_diff_to_dict(diff_list):
    result = {}
    for item in diff_list:
        match item['flag']:
            case 'added':
                result['+ ' + item['key']] = item['new_value']
            case 'removed':
                result['- ' + item['key']] = item['old_value']
            case 'updated':
                result['- ' + item['key']] = item['old_value']
                result['+ ' + item['key']] = item['new_value']
            case 'same':
                result['  ' + item['key']] = item['value']
            case 'nested':
                result['  ' + item['key']] = convert_diff_to_dict(
                    item['children'])
    return result


def stringify(data, replacer=' ', spaces_count=1):
    def iter_(current_value, depth, default_special_symbol=replacer * 2):
        if not isinstance(current_value, dict):
            if isinstance(current_value, bool):
                return str(current_value).lower()
            elif current_value is None:
                return 'null'
            return str(current_value)

        end_indent = replacer * (depth * spaces_count)
        lines = []
        special_symbols = ['  ', '+ ', '- ']
        for key, value in current_value.items():
            special_symbol = '' if key[:2] in special_symbols else (
                default_special_symbol)
            begin_indent = replacer * ((depth + 1) * spaces_count - 2) + \
                special_symbol
            lines.append(f'{begin_indent}{key}: {iter_(value, depth + 1)}')
        result = chain("{", lines, [end_indent + "}"])
        return '\n'.join(result)

    return iter_(data, 0)


def render_stylish(diff_list):
    return stringify(convert_diff_to_dict(diff_list),
                     replacer=' ', spaces_count=4)
