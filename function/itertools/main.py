import itertools


def flatten_dict_values(data: dict):
    if data is None:
        return []
    return list(itertools.chain.from_iterable(list(data.values())))


if __name__ == "__main__":
    data = {"a": [1, 2, 3], "b": [3, 4, 5]}
    print(flatten_dict_values(data))
    pass
