import logging
import os
from datetime import datetime


if not os.path.exists("logs"):
    os.mkdir("logs")


def get_logger():

    logger = logging.getLogger("test")

    logger.setLevel(logging.INFO)


    log_file = (
        "logs/"
        + datetime.now().strftime("%Y-%m-%d")
        + ".log"
    )


    file_handler = logging.FileHandler(
        log_file,
        encoding="utf-8"
    )


    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )


    file_handler.setFormatter(formatter)


    logger.addHandler(file_handler)


    return logger