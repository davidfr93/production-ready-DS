# """
# Colorized logging example from Chapter 9.

# This demonstrates custom color formatting in Loguru.
# """

from loguru import logger
import sys

logger.remove()

logger.add(
    sys.stdout,
    colorize=True,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
            "<level>{level}</level> | <cyan>{message}</cyan>",
)


def main():
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")


if __name__ == "__main__":
    main()


# import logging
# from colorlog import ColoredFormatter
# formatter = ColoredFormatter(
#     "%(log_color)s%(asctime)s | %(levelname)s | %(message)s",
#     datefmt="%Y-%m-%d %H:%M:%S",
#     log_colors={
#     'DEBUG': 'cyan',
#     'INFO': 'green',
#     'WARNING': 'yellow',
#     'ERROR': 'red',
#     'CRITICAL': 'bold_red',
#     }
# )
# handler = logging.StreamHandler()
# handler.setFormatter(formatter)
# logger = logging.getLogger(__name__)
# logger.addHandler(handler)
# logger.setLevel(logging.DEBUG)
# logger.info("Colorized info message")


# def main():
#     logging.debug("This is a debug message")
#     logging.info("This is an info message")
#     logging.warning("This is a warning message")
#     logging.error("This is an error message")

# if __name__ == "__main__":
#     main()