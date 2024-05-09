from gendiff.formatters.stylish import stylish


def choose_formatter(format):
    if format == 'stylish':
        func = stylish
    return func