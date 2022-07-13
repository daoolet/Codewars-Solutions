def greet_developers(lst): 
    for dix in lst:
        dix['greeting'] = f"Hi {dix['firstName']}, what do you like the most about {dix['language']}?"
    return lst