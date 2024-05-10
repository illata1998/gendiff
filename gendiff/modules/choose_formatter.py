from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain


def choose_formatter(format):
    if format == 'stylish':
        func = stylish
    elif format == 'plain':
        func = plain
    return func
