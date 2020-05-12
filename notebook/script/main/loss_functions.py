def mean_square_loss_func(y_actual, y_predicted):
    return ((y_actual[0, 0] - y_predicted[0, 0]) ** 2 +
            (y_actual[0, 1] - y_predicted[0, 1]) ** 2 +
            (y_actual[0, 2] - y_predicted[0, 2]) ** 2 +
            (y_actual[0, 3] - y_predicted[0, 3]) ** 2 +
            (y_actual[0, 4] - y_predicted[0, 4]) ** 2 +
            (y_actual[0, 5] - y_predicted[0, 5]) ** 2 +
            (y_actual[0, 6] - y_predicted[0, 6]) ** 2 +
            (y_actual[0, 7] - y_predicted[0, 7]) ** 2 +
            (y_actual[0, 8] - y_predicted[0, 8]) ** 2 +
            (y_actual[0, 9] - y_predicted[0, 9]) ** 2 +
            (y_actual[0, 10] - y_predicted[0, 10]) ** 2 +
            (y_actual[0, 11] - y_predicted[0, 11]) ** 2 +
            (y_actual[0, 12] - y_predicted[0, 12]) ** 2 +
            (y_actual[0, 13] - y_predicted[0, 13]) ** 2 +
            (y_actual[0, 14] - y_predicted[0, 14]) ** 2 +
            (y_actual[0, 15] - y_predicted[0, 15]) ** 2 +
            (y_actual[0, 16] - y_predicted[0, 16]) ** 2 +
            (y_actual[0, 17] - y_predicted[0, 17]) ** 2 +
            (y_actual[0, 18] - y_predicted[0, 18]) ** 2) / 18


def mean_proportional_loss_func(y_actual, y_predicted):
    return (abs(y_actual[0, 0] - y_predicted[0, 0]) +
            abs(y_actual[0, 1] - y_predicted[0, 1]) +
            abs(y_actual[0, 2] - y_predicted[0, 2]) +
            abs(y_actual[0, 3] - y_predicted[0, 3]) +
            abs(y_actual[0, 4] - y_predicted[0, 4]) +
            abs(y_actual[0, 5] - y_predicted[0, 5]) +
            abs(y_actual[0, 6] - y_predicted[0, 6]) +
            abs(y_actual[0, 7] - y_predicted[0, 7]) +
            abs(y_actual[0, 8] - y_predicted[0, 8]) +
            abs(y_actual[0, 9] - y_predicted[0, 9]) +
            abs(y_actual[0, 10] - y_predicted[0, 10]) +
            abs(y_actual[0, 11] - y_predicted[0, 11]) +
            abs(y_actual[0, 12] - y_predicted[0, 12]) +
            abs(y_actual[0, 13] - y_predicted[0, 13]) +
            abs(y_actual[0, 14] - y_predicted[0, 14]) +
            abs(y_actual[0, 15] - y_predicted[0, 15]) +
            abs(y_actual[0, 16] - y_predicted[0, 16]) +
            abs(y_actual[0, 17] - y_predicted[0, 17]) +
            abs(y_actual[0, 18] - y_predicted[0, 18])) / 18
