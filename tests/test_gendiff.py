import json
from pathlib import Path


from gendiff.scripts.gendiff import  gendiff


def get_test_data_path(filename):
    return Path(__file__).parent / 'test_data' / filename


def read_file(filename):
    return open(get_test_data_path(filename))


def test_gendiff_json():
    file1 = get_test_data_path('file1.json')
    file2 = get_test_data_path('file2.json')
    expected = read_file('result.txt').read()
    actual = gendiff(file1, file2)

    assert actual == expected


def test_gendiff_yml():
    file1 = get_test_data_path('file1.yml')
    file2 = get_test_data_path('file2.yaml')
    expected = read_file('result.txt').read()
    actual = gendiff(file1, file2)

    assert actual == expected
