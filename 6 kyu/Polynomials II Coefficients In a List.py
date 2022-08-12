
def calc_poly(coef: list, x: int) -> str:
    a = ''

    if coef[0] == 0:
        if coef[1] > 1: 
            a = f"For {coef[1]}*x^{len(coef)-2} "
        elif coef[1] < -1: 
            a = f"For {coef[1]}*x^{len(coef)-2} "

        # number == 1 and number == -1
        elif coef[1] == 1: 
            a = f"For x^{len(coef)-2} "
        elif coef[1] == -1: 
            a = f"For -x^{len(coef)-2} "

        for i, v in enumerate(coef[2:]):
            power = len(coef[2:]) - 1 - i

            # when number == 1
            if v == 1 and power > 1:
                a += f"+ x^{power} "
            elif v == 1 and power == 1:
                a += f"+ x "
            # numbers > 1
            elif v > 1 and power > 1:
                a += f"+ {v}*x^{power} "
            elif v > 1 and power == 1:
                a += f"+ {v}*x "
            elif v > 0 and power == 0:
                a += f"+ {v} "

            # when number == 0
            elif v == 0:
                a += ''

            # when humber == -1
            if v == -1 and power > 1:
                a += f"- x^{power} "
            elif v == -1 and power == 1:
                a += f"- x "
            # numbers < -1
            elif v < -1 and power > 1:
                a += f"- {v * -1}*x^{power} "
            elif v < -1 and power == 1:
                a += f"- {v * -1}*x "
            elif v < 0 and power == 0:
                a += f"- {v * -1} "
    # -------------------------------------------------------------------------
    else:    
    # positive > 1 and negative < -1
        if coef[0] > 1: 
            a = f"For {coef[0]}*x^{len(coef)-1} "
        elif coef[0] < -1: 
            a = f"For {coef[0]}*x^{len(coef)-1} "

        # number == 1 and number == -1
        elif coef[0] == 1: 
            a = f"For x^{len(coef)-1} "
        elif coef[0] == -1: 
            a = f"For -x^{len(coef)-1} "

        for i, v in enumerate(coef[1:]):
            power = len(coef[1:]) - 1 - i

            # when number == 1
            if v == 1 and power > 1:
                a += f"+ x^{power} "
            elif v == 1 and power == 1:
                a += f"+ x "
            # numbers > 1
            elif v > 1 and power > 1:
                a += f"+ {v}*x^{power} "
            elif v > 1 and power == 1:
                a += f"+ {v}*x "
            elif v > 0 and power == 0:
                a += f"+ {v} "

            # when number == 0
            elif v == 0:
                a += ''

            # when humber == -1
            if v == -1 and power > 1:
                a += f"- x^{power} "
            elif v == -1 and power == 1:
                a += f"- x "
            # numbers < -1
            elif v < -1 and power > 1:
                a += f"- {v * -1}*x^{power} "
            elif v < -1 and power == 1:
                a += f"- {v * -1}*x "
            elif v < 0 and power == 0:
                a += f"- {v * -1} "
    
    
    total = 0
    for i, v in enumerate(coef[:-1]):
        total += v * (x ** (len(coef) - 1 - i))

    a += f"with x = {x} the value is {total + coef[-1]}"

    return a

print(calc_poly([0, -16, 15, -17, 41], -84))