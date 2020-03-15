def proportional_loss_func(y_actual, y_predicted):
    return abs((y_actual[0, 0] - y_predicted[0, 0]) +
               abs(y_actual[0, 1] - y_predicted[0, 1]) +
               abs(y_actual[0, 2] - y_predicted[0, 2]) +
               abs(y_actual[0, 3] - y_predicted[0, 3]) +
               abs(y_actual[0, 4] - y_predicted[0, 4]) +
               abs(y_actual[0, 5] - y_predicted[0, 5]) +
               abs(y_actual[0, 6] - y_predicted[0, 6]) +
               abs(y_actual[0, 25] - y_predicted[0, 25]) +
               abs(y_actual[0, 26] - y_predicted[0, 26]) +
               abs(y_actual[0, 27] - y_predicted[0, 27]) +
               abs(y_actual[0, 28] - y_predicted[0, 28]) +
               abs(y_actual[0, 29] - y_predicted[0, 29]) +
               abs(y_actual[0, 30] - y_predicted[0, 30]) +
               abs(y_actual[0, 31] - y_predicted[0, 31]) +
               abs(y_actual[0, 32] - y_predicted[0, 32]) +
               abs(y_actual[0, 33] - y_predicted[0, 33]) +
               abs(y_actual[0, 34] - y_predicted[0, 34])) / 17


def mean_square_loss_func(y_actual, y_predicted):
    return ((y_actual[0, 0] - y_predicted[0, 0]) ** 2 +
            (y_actual[0, 1] - y_predicted[0, 1]) ** 2 +
            (y_actual[0, 2] - y_predicted[0, 2]) ** 2 +
            (y_actual[0, 3] - y_predicted[0, 3]) ** 2 +
            (y_actual[0, 4] - y_predicted[0, 4]) ** 2 +
            (y_actual[0, 5] - y_predicted[0, 5]) ** 2 +
            (y_actual[0, 6] - y_predicted[0, 6]) ** 2 +
            (y_actual[0, 25] - y_predicted[0, 25]) ** 2 +
            (y_actual[0, 26] - y_predicted[0, 26]) ** 2 +
            (y_actual[0, 27] - y_predicted[0, 27]) ** 2 +
            (y_actual[0, 28] - y_predicted[0, 28]) ** 2 +
            (y_actual[0, 29] - y_predicted[0, 29]) ** 2 +
            (y_actual[0, 30] - y_predicted[0, 30]) ** 2 +
            (y_actual[0, 31] - y_predicted[0, 31]) ** 2 +
            (y_actual[0, 32] - y_predicted[0, 32]) ** 2 +
            (y_actual[0, 33] - y_predicted[0, 33]) ** 2 +
            (y_actual[0, 34] - y_predicted[0, 34]) ** 2) / 17
