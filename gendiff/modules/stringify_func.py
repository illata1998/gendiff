from itertools import chain


def stringify(value, replacer=' ', spaces_count=1):

    def iter_(current_value, depth):
        if not isinstance(current_value, dict)
            if isinstance(current_value, bool):
                return str(current_value).lower()
            return str(current_value)

        deep_indent_size = depth + spaces_count
        deep_indent = replacer * deep_indent_size
        current_indent = replacer * depth
        lines = []
        for key, val in current_value.items():
            lines.append(f'{deep_indent}{key}: {iter_(val, deep_indent_size)}')
        result = chain("{", lines, [current_indent + "}"])
        return '\n'.join(result)

    return iter_(value, 0)
