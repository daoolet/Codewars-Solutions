def max_rot(n):
    st = str(n)
    arr = [st]

    for i in range(len(st)):
        st = st[0:i] + st[i+1:] + st[i]
        arr.append(''.join(st))

    return int(max(arr))