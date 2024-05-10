from gendiff.formatters.stylish_formatter import render_stylish
from gendiff.formatters.plain_formatter import render_plain
from gendiff.formatters.json_formatter import render_json


def choose_formatter(format_name):
    match format_name:
        case 'stylish':
            return render_stylish
        case 'plain':
            return render_plain
        case 'json':
            return render_json
