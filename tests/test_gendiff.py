import json
from pathlib import Path


from gendiff.scripts.gendiff import  gendiff


def get_test_data_path(filename):
    return Path(__file__).parent / 'test_data' / filename


def read_file(filename):
    return open(get_test_data_path(filename))


def test_gendiff():
    file1 = json.load(read_file('file1.json'))
    file2 = json.load(read_file('file2.json'))
    expected = read_file('result.txt').read()
    actual = gendiff(file1, file2)

    assert actual == expected
