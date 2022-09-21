import os
import json
import pickle
from tqdm import tqdm


def read_data(filename):
    data = []
    with open(filename) as f:
        for line in f:
            train0 = json.loads(line)
            data.append(train0)
    return data


def dict_create(data, valid_data, test_data):
    tokens = []
    dict = {}
    for data_json in tqdm(data, desc="Creating dictionary on train data"):
        abstract = data_json['abstract']
        keywords = data_json['keywords']
        tokens += [i for i in abstract.split()]
        tokens += [j for i in keywords for j in i.split()]
    for data_json in tqdm(valid_data, desc="Creating dictionary on valid data"):
        abstract = data_json['abstract']
        keywords = data_json['keywords']
        tokens += [i for i in abstract.split()]
        tokens += [j for i in keywords for j in i.split()]
    for data_json in tqdm(test_data, desc="Creating dictionary on test data"):
        abstract = data_json['abstract']
        keywords = data_json['keywords']
        tokens += [i for i in abstract.split()]
        tokens += [j for i in keywords for j in i.split()]
    tokens = set(tokens)
    for id, token in enumerate(tokens):
        dict[token] = id
    return dict


def dict_save(dict, target_name):
    with open(target_name, 'wb') as f:
        print(f"Saving {target_name}")
        pickle.dump(dict, f)


def dict_get(filename):
    with open(filename, "rb") as f:
        dict = pickle.load(f)
    return dict


def tokens_get(data):
    tokens = []
    y_tokens = []
    for data_json in data:
        abstract = data_json['abstract']
        keywords = data_json['keywords']
        tokens.append(abstract.split())
        y_tokens.append([j for i in keywords for j in i.split()])
    return tokens, y_tokens


def tokens_to_ids(data, dict):
    tokens, y_tokens = tokens_get(data)
    ids = []
    y_ids = []
    temp = []
    for sentence in tqdm(tokens, desc="Converting tokens to ids..."):
        for token in sentence:
            temp.append(dict[token])
        ids.append(temp)
        temp = []
    for sentence in tqdm(y_tokens, desc="Converting y to ids..."):
        for token in sentence:
            temp.append(dict[token])
        y_ids.append(temp)
        temp = []
    return ids, y_ids


def ids_save(train_ids, train_y_ids, valid_ids, valid_y_ids, test_ids, test_y_ids, target_name):
    data = {
        "train_ids": train_ids,
        "train_y_ids": train_y_ids,
        "valid_ids": valid_ids,
        "valid_y_ids": valid_y_ids,
        "test_ids": test_ids,
        "test_y_ids": test_y_ids,
    }
    with open(target_name, "wb") as f2:
        print(f"Saving train ids {target_name}")
        pickle.dump(data, f2)


def process():
    data = read_data("./dataset/train-0.json")
    valid_data = read_data("./dataset/valid.json")
    test_data = read_data("./dataset/test.json")
    dict = dict_create(data, valid_data, test_data)
    dict_name = "./hot_data/dict.pkl"
    input_name = "./hot_data/input_ids.pkl"
    if not os.path.exists(dict_name):
        dict_save(dict, dict_name)
    if not os.path.exists(input_name):
        ids, y = tokens_to_ids(data, dict)
        valid_ids, valid_y_ids = tokens_to_ids(valid_data, dict)
        test_ids, test_y_ids = tokens_to_ids(test_data, dict)
        ids_save(
            train_ids=ids,
            train_y_ids=y,
            valid_ids=valid_ids,
            valid_y_ids=valid_y_ids,
            test_ids=test_ids,
            test_y_ids=test_y_ids,
            target_name=input_name,
        )


if __name__ == '__main__':
    process()
