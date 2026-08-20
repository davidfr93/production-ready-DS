"""
Basic Loguru logging example from Chapter 9.

This demonstrates the elegant out-of-the-box functionality of Loguru.
"""

import logging

logging.basicConfig(level=logging.DEBUG)


def main():
    logging.debug("This is a debug message")
    logging.info("This is an info message")
    logging.warning("This is a warning message")
    logging.error("This is an error message")

if __name__ == "__main__":
    main()


from loguru import logger

def main():
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")


if __name__ == "__main__":
    main()