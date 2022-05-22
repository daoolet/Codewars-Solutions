def make_backronym(acronym):
    s = ''
    for i in acronym:
        s += ''.join(dictionary[i.upper()])
        s += ' '
        
    return s[:-1]