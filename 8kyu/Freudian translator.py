def to_freud(sentence):
    return ("sex "*sum(1 for i in sentence.split()))[:-1]