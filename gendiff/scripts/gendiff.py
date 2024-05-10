#!/user/bin/env python3


from gendiff.modules.generate_diff import generate_diff
from gendiff.cli import parse


def main():
    args = parse()
    print(generate_diff(args.first_file, args.second_file,
                        format_name=args.format))


if __name__ == '__main__':
    main()
