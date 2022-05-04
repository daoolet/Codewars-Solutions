def get_count(sentence):
    c = 0
    for i in sentence:
        if i in 'aeuio':
            c+=1
    return c