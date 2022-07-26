def run_length_encoding(s: str):
    res = []
    count = 1
    
    if len(s) == 0:
        return res
    
    char = s[0]

    for i in range(1, len(s)):
        if s[i] == char:
            count += 1
        else:
            res.append([count, char])
            char = s[i]
            count = 1
    res.append([count, char])

    return res