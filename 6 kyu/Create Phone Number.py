def create_phone_number(array: list) -> str:
    a = ''.join(map(str,array))
    return f"({a[:3]}) {a[3:6]}-{a[6:]}"

print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])) # "(123) 456-7890"