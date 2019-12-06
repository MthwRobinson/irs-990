import logging

import daiquiri


def get_logger(filename):
    """Configures the logger for the specified file."""
    daiquiri.setup(level=logging.INFO)
    return daiquiri.getLogger(filename)
