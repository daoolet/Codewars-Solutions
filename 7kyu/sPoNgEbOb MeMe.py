
def sponge_meme(s):
    return ''.join(s[i].lower() if i%2 else s[i].upper() for i in range(len(s)))
