def diff(data1, data2):
    result = []
    keys = set(data1.keys()) | set(data2.keys())
    for key in keys:
        if key not in data1:
            result.append({
                'key': key,
                'flag': 'added',
                'new_value': data2[key]
            })
        elif key not in data2:
            result.append({
                'key': key,
                'flag': 'removed',
                'old_value': data1[key],
            })
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            result.append({
                'key': key,
                'flag': 'nested',
                'children': diff(data1[key], data2[key])
            })
        elif data1[key] == data2[key]:
            result.append({
                'key': key,
                'flag': 'same',
                'value': data1[key]
            })
        else:
            result.append({
                'key': key,
                'flag': 'updated',
                'old_value': data1[key],
                'new_value': data2[key]
            })
    return sorted(result, key=lambda item: item['key'])
