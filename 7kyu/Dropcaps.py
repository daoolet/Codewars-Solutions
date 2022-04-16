def drop_cap(str_):
    return ' '.join(i.title() if len(i) > 2 else i for i in str_.split(' '))