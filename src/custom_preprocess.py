import unittest
import csv
from datetime import datetime, timedelta


def load_raw_data_and_split_by_dt(path, output_dir):
    base_datetime = datetime.strptime('141021', '%y%m%d')
    output_file_dict = {(base_datetime + timedelta(days=x)).strftime('%y%m%d'): open(
        output_dir + '/' + (base_datetime + timedelta(days=x)).strftime('%y%m%d') + '.csv', 'w') for x in range(0, 10)}

    with open(path, 'rb') as csvfile:
        header = csvfile.readline()
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            hour_column = row[2]
            dt = hour_column[:6]
            hour = hour_column[6:]
            output_file_dict[dt].write(",".join(row[:2] + [hour] + row[3:]) + "\n")


class TestCustomPreprocess(unittest.TestCase):
    def test_load_raw_data_and_split_by_dt(self):
        load_raw_data_and_split_by_dt('../fixtures/train.thumb', '../fixtures')


if __name__ == '__main__':
    unittest.main()
