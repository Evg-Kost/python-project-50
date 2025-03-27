def normalize(value):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    else:
        return value


def check_type(values, level):
    result = []
    predict = level * '    '
    if isinstance(values, dict):
        for key in values:
            result.append(f'{predict}{key}: {check_type(values[key], level + 1)}')
    else:
        return normalize(values)
    return '{\n' + '\n'.join(result) + '\n' + predict[:-4] + '}'


def stylish(data, level=1):
    items = []
    predict = level * '    '
    for key, value in data.items():
        match value.get('status', ):
            case 'added':
                items.append(f'{predict[:-2]}+ {key}: {check_type(value["value"], level + 1)}')
            case 'deleted':
                items.append(f'{predict[:-2]}- {key}: {check_type(value["value"], level + 1)}')
            case 'update':
                items.append(f'{predict[:-2]}- {key}: {check_type(value["old_value"], level + 1)}')
                items.append(f'{predict[:-2]}+ {key}: {check_type(value["new_value"], level + 1)}')
            case 'no_change':
                items.append(f'{predict[:-2]}  {key}: {check_type(value["value"], level + 1)}')
            case 'nested':
                items.append(f'{predict[:-2]}  {key}: {stylish(value["value"], level + 1)}')
            case _:
                print('error', value)
    return '{\n' + '\n'.join(items) + '\n' + predict[:-4] + '}'
