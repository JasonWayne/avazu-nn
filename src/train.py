import keras

root_dir = '/home/jason/code/avazu-nn/fixtures/'

X_train = []
y_train = []

X_test = []
y_test = []

with open(root_dir + 'train_hashed_1024.txt', 'rb') as f:
    for line in f:
        row = map(lambda x: int(x), line.strip().split(","))
        X_train.append(row[1:])
        y_train.append(row[0])

with open(root_dir + 'test_hash_1024.txt', 'rb') as f:
    for row in f:
        row = map(lambda x: int(x), line.strip().split(","))
        X_test.append(row[1:])
        y_test.append(row[0])
