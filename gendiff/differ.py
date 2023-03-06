from gendiff.constants import ADDED, NESTED, CHANGED, UNCHANGED, DELETED


def build_diff(value_1, value_2):  # noqa:C901
    def inner(node_1, node_2):
        keys = node_1.keys() | node_2.keys()
        result = {}
        result_list = []
        for key in keys:
            result_list.append(key)
        for key in sorted(result_list):
            if key in node_1 \
                    and key in node_2 \
                    and isinstance(node_1[key], dict) \
                    and isinstance(node_2[key], dict):
                result[key] = {'status': NESTED,
                               'value': inner(node_1[key], node_2[key])}
            else:
                if key not in node_1:
                    result[key] = {'status': ADDED, 'value': node_2[key]}
                elif key not in node_2:
                    result[key] = {'status': DELETED, 'value': node_1[key]}
                elif node_1[key] == node_2[key]:
                    result[key] = {'status': UNCHANGED, 'value': node_1[key]}
                else:
                    result[key] = {'status': CHANGED, 'value_1': node_1[key],
                                   'value_2': node_2[key]}
        return result
    return inner(value_1, value_2)
