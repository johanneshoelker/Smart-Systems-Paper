import torch
import tasks
from ts2vec import TS2Vec


# (Both train_data and test_data have a shape of n_instances x n_timestamps x n_features)
dev = torch.device('cpu')

# Train a TS2Vec model
model = TS2Vec(
    input_dims=1,
    device=dev,
    output_dims=320
)

import pandas as pd
import numpy as np
from smadata import getSMAData

def preprocess_SMA(xtrain_dfs, xtest_dfs, ytrain_dfs, ytest_dfs):
    all_train_data = pd.concat(xtrain_dfs.values())
    all_test_data = pd.concat(xtest_dfs.values())

    mean = np.nanmean(all_train_data)
    std = np.nanstd(all_train_data)

    train_data_list = []
    train_labels_list = []
    test_data_list = []
    test_labels_list = []

    for inv in xtrain_dfs.keys():
        xtrain = xtrain_dfs[inv].values.astype(np.float64)
        xtest = xtest_dfs[inv].values.astype(np.float64)
        ytrain = ytrain_dfs[inv].values.flatten()
        ytest = ytest_dfs[inv].values.flatten()

        xtrain = (xtrain - mean) / std
        xtest = (xtest - mean) / std

        train_data_list.append(xtrain[..., np.newaxis])
        train_labels_list.append(ytrain)
        test_data_list.append(xtest[..., np.newaxis])
        test_labels_list.append(ytest)

    # Concatenate all inverter data into single arrays
    train_data = np.concatenate(train_data_list, axis=0)
    train_labels = np.concatenate(train_labels_list, axis=0)
    test_data = np.concatenate(test_data_list, axis=0)
    test_labels = np.concatenate(test_labels_list, axis=0)

    return train_data, train_labels, test_data, test_labels

xtrain_dfs, xtest_dfs, ytrain_dfs, ytest_dfs = getSMAData()
train_data, train_labels, test_data, test_labels = preprocess_SMA(xtrain_dfs, xtest_dfs, ytrain_dfs, ytest_dfs)

test_repr = model.encode(test_data)  # n_instances x n_timestamps x output_dims

print(test_repr)
