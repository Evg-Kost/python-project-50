import argparse
import json

from gendiff.comare_files import compare_files


def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference.")
    parser.add_argument("first_file", type=str)
    parser.add_argument("second_file", type=str)
    parser.add_argument("-f", "--format", help="set format of output")
    args = parser.parse_args()
    # print(args)
    file1 = json.load(open(
	'/home/evgeny/PycharmProjects/PythonProject/python-project-50/input_file/'
         + args.first_file))
    file2 = json.load(open(
	'/home/evgeny/PycharmProjects/PythonProject/python-project-50/input_file/'
        + args.second_file))
    # print(file1)
    # print(file2)
    print(compare_files(file1, file2))


if __name__ == "__main__":
    main()
