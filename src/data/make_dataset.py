# -*- coding: utf-8 -*-
import subprocess
import feather
import pandas as pd
import pathlib


class Dataset():

    def __init__(self, d_path='./data/'):
        self._d_path = pathlib.Path(d_path)

    def download_data(self, comp_name=''):
        self._comp_name = comp_name
        # Download dataset from kaggle using kaggle api
        try:
            subprocess.check_call(
                "kaggle competitions download -c \
                {} -p ./data/raw/".format(self._comp_name)
                )
        except:
            print("subprocess.check_call() failed")

    def get_train_test(self):
        raw_p = self._d_path / 'raw'                 # raw dir path
        self._trf_l = list(raw_p.glob('*.ftr'))      # feather files list
        self._csv_l = list(raw_p.glob('*.csv'))      # csv files list

        if(len(self._trf_l) == 0):

            if(len(self._csv_l) != 0):
                train_df = pd.read_csv("./data/raw/train.csv")
                test_df = pd.read_csv("./data/raw/test.csv")
            else:
                print('csv file not exist')

            feather.write_dataframe(train_df, "./data/raw/train.ftr")
            feather.write_dataframe(test_df, "./data/raw/test.ftr")
            print('Feather file created')

        else:
            train_df = feather.read_dataframe("./data/raw/train.ftr")
            test_df = feather.read_dataframe("./data/raw/test.ftr")

        return train_df, test_df

    def get_trf_list(self):
        return self._trf_l

    def get_csv_list(self):
        return self._csv_l

    def get_comp_name(self):
        return self._comp_name

    def get_data_path(self):
        return str(self._d_path)
