import logging

import pandas as pd

from utils.load_dataframe import save_pd


def load(data, file_path):
    save_pd(data[["Date", "Price"]], file_path)
