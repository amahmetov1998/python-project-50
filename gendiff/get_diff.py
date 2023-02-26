from pprint import pprint

a = {
  "common": {
    "setting1": "Value 1",
    "setting2": 200,
    "setting3": True,
    "setting6": {
      "key": "value",
      "doge": {
        "wow": ""
      }
    }
  },
  "group1": {
    "baz": "bas",
    "foo": "bar",
    "nest": {
      "key": "value"
    }
  },
  "group2": {
    "abc": 12345,
    "deep": {
      "id": 45
    }
  }
}

b = {
  "common": {
    "follow": False,
    "setting1": "Value 1",
    "setting3": {
      "key": "value"
    },
    "setting4": "blah blah",
    "setting5": {
      "key5": "value5"
    },
    "setting6": {
      "key": "value",
      "ops": "vops",
      "doge": {
        "wow": "so much"
      }
    }
  },
  "group1": {
    "foo": "bar",
    "baz": "bars",
    "nest": "str"
  },
  "group3": {
    "deep": {
      "id": {
        "number": 45
      }
    },
    "fee": 100500
  }
}



def make_diff(nested_1, nested_2):  # noqa: C901
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
                result[key] = inner(node_1[key], node_2[key])
            else:
                if key not in node_1:
                    result[key] = {'status': 'added', 'value': node_2[key]}
                elif key not in node_2:
                    result[key] = {'status': 'deleted', 'value': node_1[key]}
                elif node_1[key] == node_2[key]:
                    result[key] = {'status': 'unchanged', 'value': node_1[key]}
                else:
                    result[key] = {'status': 'changed', 'value_1': node_1[key],
                                   'value_2': node_2[key]}
        return result
    return inner(nested_1, nested_2)

pprint(make_diff(a, b))