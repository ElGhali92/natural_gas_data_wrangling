import re
from datetime import datetime

import numpy as np
from pandas.core.base import DataError

import settings


def rename_natural_gas_columns(data):
    data = data.rename(columns=lambda x: "Price" if re.search("Price", x) else x)
    return data


def transform_date_column(data, granularity):
    if granularity == "monthly":
        data["Date"] = data["Date"].apply(lambda d: d.replace(day=1))
    elif granularity == "annual":
        data["Date"] = data["Date"].apply(lambda d: d.replace(day=1, month=1))
    return data


def year_week(data):
    data["week_number"] = data["Date"].dt.week
    data["week_number"] = data["week_number"].apply(str)
    data["year-week"] = (
        data["Date"].apply(lambda x: str(x.year)) + "-" + data["week_number"]
    )
    return data


def fill_daily_missing_values(data):
    price_array = np.array(data["Price"])
    missing_values_pos = list(np.where(np.isnan(price_array)))
    data = year_week(data)
    for i in missing_values_pos:
        yw = data.loc[i, "year-week"]
        subdata = data[data["year-week"] == yw]
        filling_value = subdata["Price"].mean()
        data.iloc[i]["Price"] = filling_value
    return data


def fill_weekly_missing_values(data):
    data["year_month"] = data["Date"].apply(lambda x: str(x.year) + "-" + str(x.month))
    price_array = np.array(data["Price"])
    missing_values_pos = list(np.where(np.isnan(price_array)))
    for i in missing_values_pos:
        ym = data.loc[i, "year-month"]
        subdata = data[data["year-month"] == ym]
        filling_value = subdata["Price"].mean()
        data.iloc[i]["Price"] = filling_value
    return data


def fill_monthly_missing_values(data):
    data["year"] = data["Date"].dt.year.apply(str)
    price_array = np.array(data["Price"])
    missing_values_pos = list(np.where(np.isnan(price_array)))
    for i in missing_values_pos:
        y = data.loc[i, "year"]
        subdata = data[data["year"] == y]
        filling_value = subdata["Price"].mean()
        data.iloc[i]["Price"] = filling_value
    return data


def price_missing_values(data, granularity):
    if settings.price_missing_values == "drop":
        data = data.dropna()
        return data
    else:
        if granularity == "daily":
            data = fill_daily_missing_values(data)
            return data
        elif granularity == "weekly":
            data = fill_weekly_missing_values(data)
            return data
        elif granularity == "monthly":
            data = fill_monthly_missing_values(data)
            return data
        else:
            filling_value = data["Price"].mean()
            data["Price"] = data["Price"].fillna(value=filling_value)
            return data


def transform(data, granularity):
    data = rename_natural_gas_columns(data)
    data = transform_date_column(data, granularity)
    data = price_missing_values(data, granularity)
    return data
