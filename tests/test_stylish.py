from pathlib import Path


from gendiff.scripts.gendiff import gendiff


def get_test_data_path(filename):
    return Path(__file__).parent / 'test_data' / filename


def read_file(filename):
    return open(get_test_data_path(filename))


def test_gendiff_flat_json():
    file1 = get_test_data_path('flat/file1.json')
    file2 = get_test_data_path('flat/file2.json')
    expected = read_file('result_flat_stylish.txt').read()
    actual = gendiff(file1, file2)

    assert actual == expected


def test_gendiff_flat_yml():
    file1 = get_test_data_path('flat/file1.yml')
    file2 = get_test_data_path('flat/file2.yaml')
    expected = read_file('result_flat_stylish.txt').read()
    actual = gendiff(file1, file2)

    assert actual == expected


def test_gendiff_nested_json():
    file1 = get_test_data_path('nested/file1_7.json')
    file2 = get_test_data_path('nested/file2_7.json')
    expected = read_file('result_nested_stylish.txt').read()
    actual = gendiff(file1, file2)

    assert actual == expected


def test_gendiff_nested_yml():
    file1 = get_test_data_path('nested/file1_7.yml')
    file2 = get_test_data_path('nested/file2_7.yaml')
    expected = read_file('result_nested_stylish.txt').read()
    actual = gendiff(file1, file2)

    assert actual == expected



