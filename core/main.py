import logging

from core.extract_natural_gas_data import get_natural_gas_data
from core.load_natural_gas_data import load
from core.transform_natural_gas_data import transform
from utils.logging_setup import set_up_stream_logger


def main(granularity, path):

    gas_price_logger = logging.getLogger("gas_price_logger")

    gas_price_logger.info(f"Extracting {granularity} gas prices data")
    data = get_natural_gas_data(granularity)

    gas_price_logger.info(f"Transforming {granularity} gas prices data")
    data = transform(data, granularity)

    gas_price_logger.info(f"Loading {granularity} gas prices data into {path}")
    load(data, path)
