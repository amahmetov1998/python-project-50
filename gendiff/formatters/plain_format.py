def get_plain(value):  # noqa: C901
    for key, val in value.items():
        if isinstance(val, dict):
            get_plain(val)
        elif isinstance(val, bool):
            value[key] = str(val).lower()
        elif val is None:
            value[key] = 'null'

    def iter(current_value, string):
        if not isinstance(current_value, dict):
            return str(current_value)

        result_list = []
        for key, val in current_value.items():
            if isinstance(val, int):
                result_list.append(f'{key}: {val}')
            elif 'status' in val and 'value_1' not in val \
                    and not isinstance(val['value'], dict):
                if val['status'] == 'added':
                    result_list.append(
                        f"""Property '{string}{key}' was added with value: '{
                        val["value"]}'"""
                    )
                elif val['status'] == 'deleted':
                    result_list.append(
                        f"""Property '{string}{key}' was removed"""
                    )
            elif 'status' in val \
                    and 'value_1' in val \
                    and not isinstance(val['value_1'], dict)\
                    and not isinstance(val['value_2'], dict):
                result_list.append(
                    f"""Property '{string}{key}' was updated. From '{
                    val["value_1"]}' to '{val["value_2"]}'"""
                )
            elif 'status' in val \
                    and 'value_1' in val \
                    and isinstance(val['value_1'], dict) \
                    and not isinstance(val['value_2'], dict):
                result_list.append(
                    f"""Property '{string}{key
                    }' was updated. From [complex value] to '{
                    val["value_2"]}'"""
                )
            elif 'status' in val \
                    and 'value_1' in val \
                    and not isinstance(val['value_1'], dict) \
                    and isinstance(val['value_2'], dict):
                result_list.append(
                    f"""Property '{
                    string}{key}' was updated. From '{
                    val["value_1"]}' to [complex value]"""
                )
            elif 'status' in val and isinstance(val['value'], dict):
                if val['status'] == 'added':
                    result_list.append(
                        f'''Property '{string}{
                        key}' was added with value: [complex value]'''
                    )
                elif val['status'] == 'deleted':
                    result_list.append(
                        f'''Property '{string}{key}' was removed'''
                    )
                elif val['status'] == 'changed':
                    result_list.append(
                        f'''Property '{string}{key}' was updated. From {iter(
                            val["value_1"], string=string + f"{key}.")} to {
                        iter(val["value_2"], string = string + f"{key}.")}'''
                    )
            else:
                result_list.append(
                    iter(val, string=string + f"{key}.")
                )
        string = '\n'.join(result_list)
        return string.replace(
            "'false'", "false").replace(
            "'true'", "true").replace(
            "'null'", "null"
        )
    return iter(value, '')
