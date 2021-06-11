import logging
from pathlib import Path

from tqdm import tqdm

import settings
from core.main import main
from utils.logging_setup import set_up_stream_logger

Path(settings.output_dir).mkdir(parents=True, exist_ok=True)

gas_price_logger = set_up_stream_logger(logging.INFO, "gas_price_logger")

# Add progress bar for every granularity
granularities = ["daily", "weekly", "monthly", "annual"]
for granularity in tqdm(granularities):
    main(
        granularity,
        f"{settings.output_dir}natural_gas_{granularity}_prices.{settings.output_extension}",
    )
