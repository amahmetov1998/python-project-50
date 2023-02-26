from gendiff.cli import parse
from gendiff import generate_diff
from gendiff.open_file import open_file
from gendiff.parse_file import parse_file
from gendiff.get_file_extension import get_file_extension

args = parse()

opened_file_1, opened_file_2 = open_file(args.first_file), \
    open_file(args.second_file)
extension_1, extension_2 = get_file_extension(args.first_file), \
    get_file_extension(args.second_file)
parsed_file_1, parsed_file_2 = parse_file(opened_file_1, extension_1), \
    parse_file(opened_file_2, extension_2)
diff = generate_diff(parsed_file_1, parsed_file_2, args.format)


def main():
    print(diff)


if __name__ == '__main__':
    main()
