import logging
from config import LOG_LEVEL


def setup_logger() -> logging.Logger:
    level = getattr(logging, LOG_LEVEL.upper(), logging.INFO)

    logging.basicConfig(
        level=level,
        format="%(asctime)s | %(levelname)s | %(message)s"
    )

    return logging.getLogger("cloud-janitor")