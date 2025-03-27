# import json
# import yaml

def compare_files(data1, data2):
    result = {}
    sorted_keys = sorted(data1 | data2)
    for key in sorted_keys:
        if key not in data1:
            result[key] = {'status': 'added', 'value': data2[key]}
        elif key not in data2:
            result[key] = {'status': 'deleted', 'value': data1[key]}
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            result[key] = {'status': 'nested', 'value': compare_files(data1[key], data2[key])}
        elif data1[key] != data2[key]:
            result[key] = {'status': 'update', 'old_value': data1[key], 'new_value': data2[key]}
        elif data1[key] == data2[key]:
            result[key] = {'status': 'no_change', 'value': data1[key]}
    return result

# filepath1 = {
#   "host": "hexlet.io",
#   "timeout": 50,
#   "proxy": "123.234.53.22",
#   "follow": False
# }
# filepath2 = {
#     "timeout": 20,
#     "verbose": True,
#     "host": "hexlet.io"
# }
# filepath1 = json.load(open('/home/evgeny/PycharmProjects/PythonProject/python-project-50/tests/test_data/file1_7.json'))
# filepath2 = json.load(open('/home/evgeny/PycharmProjects/PythonProject/python-project-50/tests/test_data/file2_7.json'))
#
# print(compare_files(filepath1, filepath2))
# print()
# print(stylish(compare_files(filepath1, filepath2)))