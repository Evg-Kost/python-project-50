def compare_files(file1, file2):
    new_file = {}
    for i in file1.keys():
        if i in file2:
            if file1.get(i) == file2.get(i):
                new_file['  ' + i] = file1[i]
            else:
                new_file['- ' + i] = file1[i]
                new_file['+ ' + i] = file2[i]
        else:
            new_file['- ' + i] = file1[i]
    for i in file2.keys():
        if i not in file1:
            new_file['+ ' + i] = file2[i]
    result = '{\n'
    for i in sorted(new_file.items(), key=lambda item: item[0][2:]):
        result += f'{i[0]}: {i[1]}\n'
    result += '}'
    return result


"""
file1 = {
  "host": "hexlet.io",
  "timeout": 50,
  "proxy": "123.234.53.22",
  "follow": False
}
file2 = {
  "timeout": 20,
  "verbose": True,
  "host": "hexlet.io"
}

print(compare_files(file1, file2))
"""