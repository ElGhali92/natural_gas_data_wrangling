import os

henry_hub_gas_data_source = {
    "url": os.getenv(
        "HENRY_HUB_GAS_DATA_SOURCE",
        "https://www.eia.gov/dnav/ng/hist_xls/RNGWHHD{granularity}.xls",
    ),
    "sheet_name": os.getenv("SHEET_NAME", "Data 1"),
    "header": os.getenv("HEADER", 2),
}

price_missing_values = os.getenv("PRICE_MISSING_VALUES", "drop")

output_dir = os.getenv("OUTPUT_DIR", "data/")

output_extension = os.getenv("OUTPUT_EXTENSION", "csv")
