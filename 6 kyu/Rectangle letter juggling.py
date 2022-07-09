from string import punctuation as pun

def cipher_text(s):
    
    if len(s) == 0:
        return ''

    text = "".join([i for i in s if i not in pun]).replace(" ", "").lower()
    # print(f"Splitted text {text}")

    def find_a_b(s :str):
        sqrted = len(s) ** 0.5
        sqrted_int = int(sqrted)
        # print(len(s), sqrted, sqrted_int)

        if sqrted - sqrted_int == 0:
            return sqrted_int, sqrted_int
        else:
            if sqrted_int * (sqrted_int+1) >= len(s):
                return sqrted_int, sqrted_int+1
            else:
                return sqrted_int+1, sqrted_int+1

    a, b = find_a_b(text)

    text += " " * (a*b - len(text))
    # print(f"Text: {text} |{len(text)}| a*b: {a}*{b}={a*b}")

    chunks = [text[i:i+b] for i in range(0, len(text), b)]
    # print(chunks, len(chunks))

    answer = []
    for i in range(b):
        text_rdy = ''
        for word in chunks:
            text_rdy += word[i]
        text_rdy += ' '
        answer.append(text_rdy)

    return "".join(answer)[:-1]