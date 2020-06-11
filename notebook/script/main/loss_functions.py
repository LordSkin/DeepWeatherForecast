import numpy as np
from keras.losses import mean_absolute_error, mean_squared_error


def mean_square_loss_func(y_actual, y_predicted):
    return mean_squared_error(y_actual[:, :19], y_predicted[:, :19])


def mean_proportional_loss_func(y_actual, y_predicted):
    return mean_absolute_error(y_actual[:, :19], y_predicted[:, :19])


def mean_proportional_loss_func_rev(y_actual, y_predicted):
    return mean_absolute_error(y_actual[:19, :], y_predicted[:19, :])


def error_on_series(y_actual, y_predicted):  # [n, 55]
    return np.mean(np.sum(abs(y_actual[:, :19] - y_predicted[:, :19]), axis=1) / 19)


def error_on_rain(y_actual, y_predicted):  # [n, 55]
    return np.mean(abs(y_actual[:, 0] - y_predicted[:, 0]))


def error_on_temp(y_actual, y_predicted):  # [n, 55]
    return np.mean(abs(y_actual[:, 1] - y_predicted[:, 1]))


def error_on_wetb(y_actual, y_predicted):  # [n, 55]
    return np.mean(abs(y_actual[:, 2] - y_predicted[:, 2]))


def error_on_dewpt(y_actual, y_predicted):  # [n, 55]
    return np.mean(abs(y_actual[:, 3] - y_predicted[:, 3]))


def error_on_rhum(y_actual, y_predicted):  # [n, 55]
    return np.mean(abs(y_actual[:, 4] - y_predicted[:, 4]))


def error_on_msl(y_actual, y_predicted):  # [n, 55]
    return np.mean(abs(y_actual[:, 5] - y_predicted[:, 5]))


def error_on_wdsp(y_actual, y_predicted):  # [n, 55]
    return np.mean(abs(y_actual[:, 6] - y_predicted[:, 6]))


def error_on_sun(y_actual, y_predicted):  # [n, 55]
    return np.mean(abs(y_actual[:, 7] - y_predicted[:, 7]))


def error_on_vis(y_actual, y_predicted):  # [n, 55]
    return np.mean(abs(y_actual[:, 8] - y_predicted[:, 8]))


def error_on_weather_code(y_actual, y_predicted):  # [n, 55]
    return np.mean(np.sum(abs(y_actual[:, 9:19] - y_predicted[:, 9:19]), axis=1) / 10)


def _decode_one_hot(one_hot_hour):
    return np.argmax(one_hot_hour, axis=1)


def filter_jan(vec):  # [71,55]
    return _decode_one_hot(vec[:, 0, 42:]) == 0


def filter_feb(vec):  # [71,55]
    return _decode_one_hot(vec[:, 0, 42:]) == 1


def filter_mar(vec):  # [71,55]
    return _decode_one_hot(vec[:, 0, 42:]) == 2


def filter_apr(vec):  # [71,55]
    return _decode_one_hot(vec[:, 0, 42:]) == 3


def filter_may(vec):  # [71,55]
    return _decode_one_hot(vec[:, 0, 42:]) == 4


def filter_jun(vec):  # [71,55]
    return _decode_one_hot(vec[:, 0, 42:]) == 5


def filter_jul(vec):  # [71,55]
    return _decode_one_hot(vec[:, 0, 42:]) == 6


def filter_aug(vec):  # [71,55]
    return _decode_one_hot(vec[:, 0, 42:]) == 7


def filter_sep(vec):  # [71,55]
    return _decode_one_hot(vec[:, 0, 42:]) == 8


def filter_oct(vec):  # [71,55]
    return _decode_one_hot(vec[:, 0, 42:]) == 9


def filter_nov(vec):  # [71,55]
    return _decode_one_hot(vec[:, 0, 42:]) == 10


def filter_dec(vec):  # [71,55]
    return _decode_one_hot(vec[:, 0, 42:]) == 11


def filter_winter(vec):  # [71,55]
    month = _decode_one_hot(vec[:, 0, 42:])
    return np.logical_or(np.logical_or(month == 11, month == 0), month == 1)


def filter_spring(vec):  # [71,55]
    month = _decode_one_hot(vec[:, 0, 42:])
    return np.logical_or(np.logical_or(month == 2, month == 3), month == 4)


def filter_summer(vec):  # [71,55]
    month = _decode_one_hot(vec[:, 0, 42:])
    return np.logical_or(np.logical_or(month == 5, month == 6), month == 7)


def filter_autumn(vec):  # [71,55]
    month = _decode_one_hot(vec[:, 0, 42:])
    return np.logical_or(np.logical_or(month == 8, month == 9), month == 10)


def filter_hour(vec, hour):  # [71,55]
    return _decode_one_hot(vec[:, 18:42]) == hour
