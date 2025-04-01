def normalize(value):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, dict):
        return '[complex value]'
    else:
        return f"'{value}'"


def get_plain(data: dict):
    result = []
    parents = []

    def get_line(data: dict, parents):
        for key, value in data.items():
            if isinstance(value, dict):
                if value.get('status') == 'nested':
                    parents.append(key)
                    get_line(value['value'], parents)
                    parents.pop()
                elif parents != '':
                    parents.append(key)
                    path = '.'.join(parents)
                    status = value['status']
                    if value.get('status') == 'removed':
                        result.append(f"Property '{path}' was {status}")
                    elif value.get('status') == 'updated':
                        result.append(f"Property '{path}' was {status}"
                                      f". From {normalize(value['old_value'])}"
                                      f" to {normalize(value['new_value'])}")
                    elif value.get('status') == 'added':
                        result.append(f"Property '{path}' was {status} with "
                                      f"value: {normalize(value['value'])}")
                    parents.pop()
    get_line(data, parents)

    return '\n'.join(result)
