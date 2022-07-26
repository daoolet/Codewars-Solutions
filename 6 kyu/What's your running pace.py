import math

def running_pace(distance, time):

    old_min = int(time.split(':')[0])
    old_sec = int(time.split(':')[1])
    time_converted = old_min*60 + old_sec

    time_one_km = time_converted / distance
    new_min = int(time_one_km // 60)
    new_sec = math.floor(time_one_km % 60)

    return f"{new_min}:{new_sec :02}"