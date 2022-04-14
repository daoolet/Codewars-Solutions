def longest(words):
    # Your code here
    maxim = len(words[0])
    for i in words:
        if len(i) > maxim:
            maxim = len(i)
    return maxim