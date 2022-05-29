def direction(facing, turn):
    sides = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']

    if turn > 0:
        turn = (turn-(turn//360)*360)//45 # does not work with negative degree
    else:
        turn = ((turn-(turn//360)*360)//45) - len(sides)

    for index, val in enumerate(sides): # enumerate returns 2 parameters: index and value of iterable object
        if facing == val:
            current_index = index # finding current index of origin side

    if current_index + turn >= len(sides):
        x = current_index + turn - len(sides)
    elif current_index + turn < 0:
        x = len(sides) + current_index + turn
    else:
        x = current_index + turn

    return sides[x]