def uncollapse(s):

    a = [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        "zero",
    ]

    ans = []
    l = 0
    r = l + 1

    while r <= len(s):
        chunk = s[l: r]
        if chunk in a:
            ans.append(chunk)
            l = r
            r += 1
        else:
            r += 1

    return " ".join(ans)