

import logging

class BaseTest:
    def log(self, message):
        logging.basicConfig(level=logging.INFO)
        logging.info(f"[TEST LOG] {message}")

