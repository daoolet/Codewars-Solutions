def solution(s: str) -> list:

    if len(s)%2 != 0:
        s += '_'
    return [s[i:i+2] for i in range(0, len(s), 2)]
