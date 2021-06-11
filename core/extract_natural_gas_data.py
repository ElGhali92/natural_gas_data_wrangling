from urllib.error import HTTPError

import pandas as pd

import settings


def get_natural_gas_data(granularity):
    link = settings.henry_hub_gas_data_source["url"].format(
        granularity=(granularity.lower())[0]
    )
    try:
        data = pd.read_excel(
            link,
            sheet_name=settings.henry_hub_gas_data_source["sheet_name"],
            header=settings.henry_hub_gas_data_source["header"],
        )
    except HTTPError as error:
        if error.code == 404:
            print(f"{link} url not found, please check for the correct url")
        raise
    return data
