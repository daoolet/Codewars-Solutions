def format_duration(seconds: int) -> str:

    ans = ''

# Formatting seconds
    dict_time = {}

    seconds_in_year = 60 * 60 * 24 * 365
    seconds_in_day = 60 * 60 * 24
    seconds_in_hour = 60 * 60
    seconds_in_minute = 60

    dict_time['year'] = seconds // seconds_in_year
    dict_time['day'] = (seconds - (dict_time['year'] * seconds_in_year)) // seconds_in_day
    dict_time['hour'] = (seconds - (dict_time['year'] * seconds_in_year) - 
                            (dict_time['day'] * seconds_in_day)) // seconds_in_hour
                                                                                                                    
    dict_time['minute'] = (seconds - (dict_time['year'] * seconds_in_year) - 
                            (dict_time['day'] * seconds_in_day) - 
                            (dict_time['hour'] * seconds_in_hour)) // seconds_in_minute
    dict_time['second'] = seconds % 60

    dict_time = {k:v for k,v in dict_time.items() if v > 0}
    key_list = list(dict_time)

# Proper output 
    for k,v in dict_time.items():

        if v == 1:
            ans += f"{v} {k}"
        else:
            ans += f"{v} {k}s"

        if key_list.index(k) < len(dict_time) - 2:
            ans += ', '
        elif key_list.index(k) == len(dict_time) - 2:
            ans += ' and '
        else:
            ans += ''
        
    if seconds == 0:
        return 'now'
    return ans