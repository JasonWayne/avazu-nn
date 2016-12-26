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
    for v in output_file_dict.values():
        v.close()


def load_raw_data_and_hash_and_split_by_dt(path, output_dir):
    base_datetime = datetime.strptime('141021', '%y%m%d')
    output_file_dict = {(base_datetime + timedelta(days=x)).strftime('%y%m%d'): open(
        output_dir + '/' + (base_datetime + timedelta(days=x)).strftime('%y%m%d') + "_hashed" + '.csv', 'w') for x in range(0, 10)}

    with open(path, 'rb') as csvfile:
        header = csvfile.readline()
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            hour_column = row[2]
            dt = hour_column[:6]
            hour = hour_column[6:]
            row[2] = hour
            for i in range(2, 24):
                row[i] = str(hash(row[i]) % 1024)
            output_file_dict[dt].write(",".join(row[1:]) + "\n")
    for v in output_file_dict.values():
        v.close()


def load_hash_split_train_val_test(path, output_dir):
    base_datetime = datetime.strptime('141021', '%y%m%d')
    # train = open(output_dir + '/' + 'train_hashed_1024.txt', 'w')
    # validation = open(output_dir + '/' + 'validate_hashed_1024.txt', 'w')
    #
    # with open(path, 'rb') as csvfile:
    #     header = csvfile.readline()
    #     reader = csv.reader(csvfile, delimiter=',')
    #     for row in reader:
    #         hour_column = row[2]
    #         dt = hour_column[:6]
    #         hour = hour_column[6:]
    #         row[2] = hour
    #         for i in range(2, 24):
    #             row[i] = str(hash(row[i]) % 1024 + (i - 2) * 1024)
    #         if dt >= '141130':
    #             validation.write(",".join(row[1:]) + "\n")
    #         else:
    #             train.write(",".join(row[1:]) + "\n")
    # train.close()
    # validation.close()

    test = open(output_dir + '/' + 'test_hashed_1024.txt', 'w')
    with open(path, 'rb') as f:
        header = f.readline()
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            hour_column = row[1]
            dt = hour_column[:6]
            hour = hour_column[6:]
            row[1] = hour
            for i in range(1, 23):
                row[i] = str(hash(row[i]) % 1024 + (i - 1) * 1024)
    test.close()




class TestCustomPreprocess(unittest.TestCase):
    def test_load_raw_data_and_split_by_dt(self):
        load_raw_data_and_split_by_dt('../fixtures/train.thumb', '../fixtures')

    def test_load_raw_data_and_hash_and_split_by_dt(self):
        load_raw_data_and_hash_and_split_by_dt('../fixtures/train.thumb', '../fixtures')

    def test_load_hash_split_train_val(self):
        load_hash_split_train_val_test('../fixtures/train.thumb', '../fixtures')


if __name__ == '__main__':
    unittest.main()
