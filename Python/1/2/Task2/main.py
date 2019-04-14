import json
import functools


def to_json(func):
    @functools.wraps(func)
    def dict_to_json(*args, **kwargs):
        result = func(*args, **kwargs)
        return json.dumps(result)
    return dict_to_json


@to_json
def get_data():
    return {
        'data': 42
    }


print(get_data())  # вернёт '{"data": 42}'
