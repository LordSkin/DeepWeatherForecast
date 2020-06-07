def rain_loss(y_true, y_pred):
    return abs(y_true[0, 0] - y_pred[0, 0])


def temp_loss(y_true, y_pred):
    return abs(y_true[0, 1] - y_pred[0, 1])


def wetb_loss(y_true, y_pred):
    return abs(y_true[0, 2] - y_pred[0, 2])


def dewpt_loss(y_true, y_pred):
    return abs(y_true[0, 3] - y_pred[0, 3])


def rhum_loss(y_true, y_pred):
    return abs(y_true[0, 4] - y_pred[0, 4])


def msl_loss(y_true, y_pred):
    return abs(y_true[0, 5] - y_pred[0, 5])


def wdsp_loss(y_true, y_pred):
    return abs(y_true[0, 6] - y_pred[0, 6])


def sun_loss(y_true, y_pred):
    return abs(y_true[0, 7] - y_pred[0, 7])


def vis_loss(y_true, y_pred):
    return abs(y_true[0, 8] - y_pred[0, 8])


def syn_code_loss(y_actual, y_predicted):
    return (abs(y_actual[0, 9] - y_predicted[0, 9]) +
            abs(y_actual[0, 10] - y_predicted[0, 10]) +
            abs(y_actual[0, 11] - y_predicted[0, 11]) +
            abs(y_actual[0, 12] - y_predicted[0, 12]) +
            abs(y_actual[0, 13] - y_predicted[0, 13]) +
            abs(y_actual[0, 14] - y_predicted[0, 14]) +
            abs(y_actual[0, 15] - y_predicted[0, 15]) +
            abs(y_actual[0, 16] - y_predicted[0, 16]) +
            abs(y_actual[0, 17] - y_predicted[0, 17]) +
            abs(y_actual[0, 18] - y_predicted[0, 18])) / 10
