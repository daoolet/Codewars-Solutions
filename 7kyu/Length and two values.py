def alternate(n, first_value, second_value):

    if n%2 == 0:
        return [first_value, second_value]*(n//2)
    else:
        return [first_value, second_value]*(n//2) + [first_value]
