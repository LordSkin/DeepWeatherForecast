import numpy as np


def get_next_hour(last_two_measurements):
    first_hour = _decode_one_hot(last_two_measurements[19:31, 0])
    second_hour = _decode_one_hot(last_two_measurements[19:31, 1])
    if first_hour != second_hour:
        return _encode_one_hot(second_hour)
    else:
        if second_hour < 11:
            return _encode_one_hot(first_hour + 1)
        else:
            return _encode_one_hot(0)


def _decode_one_hot(one_hou_hour):
    return np.argmax(one_hou_hour, axis=0)


def _encode_one_hot(hour):
    result = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    result[hour] = 1
    return result


def check_hours(series):
    result = []
    for measure in series.transpose():
        result.append(_decode_one_hot(measure[19:31]))
    return result
