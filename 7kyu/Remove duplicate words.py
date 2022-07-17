def remove_duplicate_words(s):
    b = []
    for i in s.split():
        if i not in b:
            b.append(i)
    return ' '.join(b)