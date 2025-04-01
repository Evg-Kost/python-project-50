from pathlib import Path


from gendiff.scripts.gendiff import  gendiff


def get_test_data_path(filename):
    return Path(__file__).parent / 'test_data' / filename


def read_file(filename):
    return open(get_test_data_path(filename))


def test_gendiff_plain():
    file1 = get_test_data_path('file1_7.json')
    file2 = get_test_data_path('file2_7.yaml')
    expected = read_file('formats/plain/result.txt').read()
    actual = gendiff(file1, file2, 'plain')

    assert actual == expected

