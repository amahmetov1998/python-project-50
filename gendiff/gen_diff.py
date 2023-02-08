import json


def generate_diff(file1, file2, file_format):
    # if file_format == 'json':
    open_file1 = json.load(open(file1))
    open_file2 = json.load(open(file2))
    # elif format == 'yaml':
    def convert_file(file):
        for key in file.keys():
            file[key] = str(file[key]).lower()
        return file
    file_1 = convert_file(open_file1)
    file_2 = convert_file(open_file2)
    space = ' '
    spisok = []
    for key in file_1:
        if key not in file_2:
            spisok_del = f'{space*2}- {key}: {file_1[key]}'
            spisok.append(spisok_del)
        elif file_1[key] != file_2[key]:
            spisok_changed_1 = f'{space*2}- {key}: {file_1[key]}'
            spisok_changed_2 = f'{space*2}+ {key}: {file_2[key]}'
            spisok.append(spisok_changed_1)
            spisok.append(spisok_changed_2)
        else:
            spisok_unchanged = f'{space*4}{key}: {file_1[key]}'
            spisok.append(spisok_unchanged)
    for key in file_2:
        if key not in file_1 and key in file_2:
            spisok_added = f'  + {key}: {file_2[key]}'
            spisok.append(spisok_added)
    sort_spisok = sorted(spisok, key=lambda x: x[4])
    final_spisok = ['{'] + sort_spisok + ['}']
    string = '\n'.join(final_spisok)
    final_string = string.replace('"', '')
    return final_string
