import argparse
import json

import yaml

from gendiff.comare_files import compare_files
from gendiff.formats.stylish import stylish


def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference.")
    parser.add_argument("first_file", type=str)
    parser.add_argument("second_file", type=str)
    parser.add_argument("-f", "--format", help="set format of output")
    args = parser.parse_args()
    print(gendiff(args.first_file, args.second_file))


def gendiff(filepath1, filepath2, format_name='stylish'):
    extension1 = filepath1.suffix
    extension2 = filepath2.suffix
    if extension1 == '.json':
        file1 = json.load(open(filepath1))
    elif extension1 == '.yml' or extension1 == '.yaml':
        file1 = yaml.safe_load(open(filepath1))
    if extension2 == '.json':
        file2 = json.load(open(filepath2))
    elif extension2 == '.yml' or extension2 == '.yaml':
        file2 = yaml.safe_load(open(filepath2))
    return stylish(compare_files(file1, file2))


if __name__ == "__main__":
    main()
