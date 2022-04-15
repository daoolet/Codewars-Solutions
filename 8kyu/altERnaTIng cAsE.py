def to_alternating_case(string):
    s = ''
    for i in string:
        if i.islower():
            s += i.upper()
        elif i.isupper():
            s += i.lower()
        else:
            s += i
    return s