def rgb(r, g, b):
    round = lambda x: min(255, max(x, 0))
    return ("{:02X}" * 2).format(round(r), round(g), round(b))


print(rgb(100, 200, -20))