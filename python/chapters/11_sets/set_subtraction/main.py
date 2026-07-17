def find_missing_ids(first_ids, second_ids):
    first_set = set(first_ids)
    second_set = set(second_ids)
    missing = first_set - second_set
    return missing
