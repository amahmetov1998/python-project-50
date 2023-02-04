from gendiff.cli import parse
from gendiff import generate_diff


args = parse()


def main():
    print(generate_diff(args.first_file, args.second_file))


if __name__ == '__main__':
    main()
