def spin_words(s: str):
    return ' '.join(i[::-1] if len(i) >= 5 else i for i in s.split())