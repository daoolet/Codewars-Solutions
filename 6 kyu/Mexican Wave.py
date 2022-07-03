

def wave(s: str):
    return [s[:i] + s[i].upper() + s[i+1:]  for i,v in enumerate(s) if v.isalpha()]

