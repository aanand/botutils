from __future__ import absolute_import
from __future__ import unicode_literals

import logging


def start_logging():
    stderr = logging.StreamHandler()
    stderr.setLevel(logging.INFO)
    stderr.setFormatter(logging.Formatter(fmt='%(levelname)8s: %(message)s'))

    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)
    root_logger.addHandler(stderr)
