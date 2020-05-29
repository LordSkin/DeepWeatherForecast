from unittest import TestCase

import numpy as np

from script.main.date_time_tools import _encode_one_hot, _decode_one_hot, get_next_hour


class Test(TestCase):

    def test_encode_one_hot_0(self):
        self.assertEqual(_encode_one_hot(0), [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    def test_encode_one_hot(self):
        self.assertEqual(_encode_one_hot(10), [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0])

    def test_decode_one_hot(self):
        self.assertEqual(_decode_one_hot([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 0)

    def test_get_next_hour_when_both_measurements_same_time(self):
        first = np.zeros(shape=37)
        first[19] = 1

        second = np.zeros(shape=37)
        second[19] = 1

        result = get_next_hour(np.array([first, second]).transpose())
        self.assertEqual(result, [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    def test_get_next_hour_when_both_measurements_different_time(self):
        first = np.zeros(shape=37)
        first[20] = 1

        second = np.zeros(shape=37)
        second[21] = 1

        result = get_next_hour(np.array([first, second]).transpose())
        self.assertEqual(result, [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    def test_get_next_hour_when_another_date(self):
        first = np.zeros(shape=37)
        first[30] = 1

        second = np.zeros(shape=37)
        second[30] = 1

        result = get_next_hour(np.array([first, second]).transpose())
        self.assertEqual(result, [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
