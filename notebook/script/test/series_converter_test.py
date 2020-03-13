import datetime
import unittest

from pandas import DataFrame

from notebook.script.main.series_converter import convert_to_time_series, convert_to_series


class TestTimeSeries(unittest.TestCase):

    def test_should_create_four_series_form_one_row(self):
        row1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]
        arg = []
        arg.append(row1)
        result = convert_to_time_series(arg)
        self.assertEqual(len(result), 4)
        self.assertEqual(result[0],
                         [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24])
        self.assertEqual(result[1],
                         [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])
        self.assertEqual(result[2],
                         [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26])
        self.assertEqual(result[3],
                         [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27])

    def test_should_create_four_series_from_2_rows(self):
        row1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
        row2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220,
                230, 240, 250]

        arg = []
        arg.append(row1)
        arg.append(row2)

        result = convert_to_time_series(arg)
        self.assertEqual(len(result), 4)
        self.assertEqual(result[0],
                         [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24])
        self.assertEqual(result[1],
                         [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])
        self.assertEqual(result[2],
                         [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200,
                          210, 220, 230, 240])
        self.assertEqual(result[3],
                         [20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210,
                          220, 230, 240, 250])

    def test_should_create_four_series_from_2_rows_with_length_3(self):
        row1 = [1, 2, 3, 4]
        row2 = [10, 20, 30, 40]

        arg = []
        arg.append(row1)
        arg.append(row2)

        result = convert_to_time_series(arg, length=3)
        self.assertEqual(len(result), 4)
        self.assertEqual(result[0],
                         [1, 2, 3])
        self.assertEqual(result[1],
                         [2, 3, 4])
        self.assertEqual(result[2],
                         [10, 20, 30])
        self.assertEqual(result[3],
                         [20, 30, 40])

    def test_should_not_create_series_if_row_to_short(self):
        row1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
        arg = []
        arg.append(row1)
        result = convert_to_time_series(arg)
        self.assertEqual(len(result), 0)

    def test_should_create_one_series_from_one_dataframe(self):
        now = datetime.datetime.now()

        dataFrame = DataFrame(
            {"hour": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 0, 1, 2],
             "day": [now, now, now, now, now, now, now, now, now, now, now, now, now, now, now, now, now, now, now, now,
                     now, now, now, now, now, now, now]})
        result = convert_to_series(dataFrame)
        self.assertEqual(len(result), 1)

    def test_should_not_create_one_series_from_one_dataframe_when_series_to_short(self):
        now = datetime.datetime.now()

        dataFrame = DataFrame(
            {"hour": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22],
             "day": [now, now, now, now, now, now, now, now, now, now, now, now, now, now, now, now, now, now, now, now,
                     now, now, now]})
        result = convert_to_series(dataFrame)
        self.assertEqual(len(result), 0)

    def test_should_create_two_series_from_one_dataframe(self):
        now = datetime.datetime.now()
        another = datetime.datetime.now() + datetime.timedelta(days=12)

        dataFrame = DataFrame(
            {"hour": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 0, 1, 2, 3,
                      4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
             "day": [now, now, now, now, now, now, now, now, now, now, now, now, now, now, now, now, now, now, now, now,
                     now, now, now, now, another, another, another, another, another, another, another, another,
                     another, another, another, another, another, another, another, another, another, another,
                     another, another, another, another, another, another]})
        result = convert_to_series(dataFrame)
        self.assertEqual(len(result), 2)

    def test_should_create_two_series_from_one_dataframe_with_length_3(self):
        now = datetime.datetime.now()
        another = datetime.datetime.now() + datetime.timedelta(days=12)

        dataFrame = DataFrame(
            {"hour": [0, 1, 2, 4, 5, 6],
             "day": [now, now, now, another, another, another]})
        result = convert_to_series(dataFrame, length=3)
        self.assertEqual(len(result), 2)


if __name__ == '__main__':
    unittest.main()
