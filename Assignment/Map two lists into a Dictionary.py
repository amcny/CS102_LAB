def map_lists_to_dict(keys, values):
    if len(keys) != len(values):
        return {}

    result_dict = {}
    for i in range(len(keys)):
        result_dict[keys[i]] = values[i]

    return result_dict
keys_list = ["Name", "Age", "City"]
values_list = ["John", 25, "New York"]

mapped_dict = map_lists_to_dict(keys_list, values_list)
print("Mapped Dictionary:", mapped_dict)