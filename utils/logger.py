# -*- coding: utf-8 -*-
import logging
import sys


def _logger(name):
    LOGGER = logging.getLogger(name)

    if not LOGGER.handlers:
        LOGGER.setLevel(logging.INFO)

        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(logging.DEBUG)
        handler.setFormatter(
            logging.Formatter(
                '[%(asctime)s] [%(levelname)s] %(message)s',
                '%Y-%m-%d %H:%M:%S'
            )
        )

        LOGGER.addHandler(handler)

    return LOGGER


logger = _logger(__name__)
