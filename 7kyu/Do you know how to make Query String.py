
def to_query_string(data):
    
    s = ''
    for k,v in data.items():
        if isinstance(v,list):
            for i in v:
                s += f"{k}={i}"
                s += '&'
        else:
            s += f"{k}={v}"
            s += '&'

    return s[:-1]

