import numpy as np
from keras.losses import mean_absolute_error, mean_squared_error


def mean_square_loss_func(y_actual, y_predicted):
    return mean_squared_error(y_actual[:, :19], y_predicted[:, :19])


def mean_proportional_loss_func(y_actual, y_predicted):
    return mean_absolute_error(y_actual[:, :19], y_predicted[:, :19])


def mean_proportional_loss_func_rev(y_actual, y_predicted):
    return mean_absolute_error(y_actual[:19, :], y_predicted[:19, :])

def error_on_series(y_actual, y_predicted):  # [n, 37]
    return np.mean(np.sum(abs(y_actual[:, :19] - y_predicted[:, :19]), axis=1) / 19)


def error_on_rain(y_actual, y_predicted):  # [n, 37]
    return np.mean(abs(y_actual[:, 0] - y_predicted[:, 0]))


def error_on_temp(y_actual, y_predicted):  # [n, 37]
    return np.mean(abs(y_actual[:, 1] - y_predicted[:, 1]))


def error_on_wetb(y_actual, y_predicted):  # [n, 37]
    return np.mean(abs(y_actual[:, 2] - y_predicted[:, 2]))


def error_on_dewpt(y_actual, y_predicted):  # [n, 37]
    return np.mean(abs(y_actual[:, 3] - y_predicted[:, 3]))


def error_on_rhum(y_actual, y_predicted):  # [n, 37]
    return np.mean(abs(y_actual[:, 4] - y_predicted[:, 4]))


def error_on_msl(y_actual, y_predicted):  # [n, 37]
    return np.mean(abs(y_actual[:, 5] - y_predicted[:, 5]))


def error_on_wdsp(y_actual, y_predicted):  # [n, 37]
    return np.mean(abs(y_actual[:, 6] - y_predicted[:, 6]))


def error_on_sun(y_actual, y_predicted):  # [n, 37]
    return np.mean(abs(y_actual[:, 7] - y_predicted[:, 7]))


def error_on_vis(y_actual, y_predicted):  # [n, 37]
    return np.mean(abs(y_actual[:, 8] - y_predicted[:, 8]))


def error_on_weather_code(y_actual, y_predicted):  # [n, 37]
    return np.mean(np.sum(abs(y_actual[:, 9:19] - y_predicted[:, 9:19]), axis=1) / 10)


def _decode_one_hot(one_hot_hour):
    return np.argmax(one_hot_hour, axis=1)


def filter_jan_feb(vec):  # [37, 71]
    return _decode_one_hot(vec[:, 30:, 0]) == 0


def filter_mar_apr(vec):  # [37, 71]
    return _decode_one_hot(vec[:, 30:, 0]) == 1


def filter_may_jun(vec):  # [37, 71]
    return _decode_one_hot(vec[:, 30:, 0]) == 2


def filter_jul_aug(vec):  # [37, 71]
    return _decode_one_hot(vec[:, 30:, 0]) == 3


def filter_sep_oct(vec):  # [37, 71]
    return _decode_one_hot(vec[:, 30:, 0]) == 4


def filter_nov_dec(vec):  # [37, 71]
    return _decode_one_hot(vec[:, 30:, 0]) == 5
