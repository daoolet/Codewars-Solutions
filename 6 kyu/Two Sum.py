def two_sum(numbers, target):
    values = {}
    for idx, val in enumerate(numbers):
        if target - val in values:
            return [values[target-val], idx]
        else:
            values[val] = idx