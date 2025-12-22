def all_eq(lst):
    max_len = 0

    # find maximum length
    for s in lst:
        if len(s) > max_len:
            max_len = len(s)

    result = []

    # pad strings with underscores
    for s in lst:
        result.append(s + "_" * (max_len - len(s)))

    return result