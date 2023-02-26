from gendiff.cli import parse
from gendiff import generate_diff


args = parse()

diff = generate_diff(args.first_file, args.second_file, args.format)


def main():
    print(diff)


if __name__ == '__main__':
    main()
