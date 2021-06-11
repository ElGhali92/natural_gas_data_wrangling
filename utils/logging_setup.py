import logging


def set_up_stream_logger(log_level, logger_name):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)
    sh = logging.StreamHandler()
    sh.setLevel(log_level)
    logger.addHandler(sh)
    return logger
