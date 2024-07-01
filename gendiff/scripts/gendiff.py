#!/usr/bin/env python3


from gendiff import start, seach_different


def main():
    args = start()
    seach_different(args.first_file, args.second_file)


if __name__ == '__main__':
    main()
