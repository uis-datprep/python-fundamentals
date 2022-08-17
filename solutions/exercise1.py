

def falling_object(time_seconds):
    if time_seconds < 0:
        raise Exception('Illegal input argument.')
    speed = 9.81 * time_seconds
    return round(0.5 * speed * time_seconds, 2)

def sum_integers(arr):
    sum = 0
    for number in arr:
        if not isinstance(number, int) or number < 0:
            raise Exception('Not a non-negative integer')
        sum += number
    return sum

def falling_object_more(time_interval, num_intervals):
    if time_interval < 1 or num_intervals < 0:
        raise Exception('Illegal input argument(s)')
    result = []
    for time_seconds in range(time_interval, time_interval*num_intervals, time_interval):
        speed = 9.81 * time_seconds
        distance = round(speed * time_seconds)
        result.append(distance)
    return result
