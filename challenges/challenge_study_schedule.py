def verify(tuple_time, target_time):
    if target_time in range(tuple_time[0], tuple_time[1] + 1):
        return 1
    else:
        return 0


def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None

    counter = 0
    for tuple_time in permanence_period:
        if type(tuple_time[0]) is not int or type(tuple_time[1]) is not int:
            return None

        counter += verify(tuple_time, target_time)

    return counter
