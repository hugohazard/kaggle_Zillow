import os
import pandas as pd


def import_data(path_to_data):
    print('Loading data ...')

    train = pd.read_csv(os.path.join(path_to_data, 'train_2016.csv'))
    prop = pd.read_csv(os.path.join(path_to_data, 'properties_2016.csv'))
    sample = pd.read_csv(os.path.join(path_to_data, 'sample_submission.csv'))
    return train, prop, sample

