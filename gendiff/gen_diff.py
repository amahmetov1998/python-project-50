import json


with open('file1.json', 'r') as file:
    file_1 = json.load(file)

with open('file2.json', 'r') as file:
    file_2 = json.load(file)

def generate_diff(file_1, file_2):
    spisok = []
    for key in file_1:
        if key not in file_2:
            spisok_del = f'- {key}: {json.dumps(file_1[key])}'
            spisok.append(spisok_del)
        elif file_1[key] != file_2[key]:
            spisok_changed_1 = f'- {key}: {json.dumps(file_1[key])}'
            spisok_changed_2 = f'+ {key}: {json.dumps(file_2[key])}'
            spisok.append(spisok_changed_1)
            spisok.append(spisok_changed_2)
        else:
            spisok_unchanged = f' {key}: {json.dumps(file_1[key])}'
            spisok.append(spisok_unchanged)
    for key in file_2:
        if key not in file_1 and key in file_2:
            spisok_added = f'+ {key}: {json.dumps(file_2[key])}'
            spisok.append(spisok_added)
    sort_spisok = sorted(spisok, key=lambda x: x[2])
    final_spisok = ['{'] + sort_spisok + ['}']
    string = '\n'.join(final_spisok)
    final_string = string.replace('"', '')
    return final_string


print(generate_diff(file_1, file_2))
