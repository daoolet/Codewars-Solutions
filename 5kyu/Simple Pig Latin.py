
def latin(s: str) -> str:
    return ' '.join(word[1:] + word[0] + "ay" if word.isalpha() else word for word in s.split())
