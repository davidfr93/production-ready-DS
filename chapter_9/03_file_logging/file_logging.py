"""
File logging example from Chapter 9.
This demonstrates logging to both terminal and file simultaneously.
"""

from loguru import logger

# Add file handler (terminal logging is default)
logger.add(
    "info.log",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | "
           "{module}:{function}:{line} - {message}",
    level="INFO",
)



def main():
    logger.debug("This debug message won't be saved to file (level=INFO)")
    logger.info("This message appears in both terminal and file")
    logger.warning("This warning appears in both terminal and file")
    logger.error("This error appears in both terminal and file")


if __name__ == "__main__":
    main()






# import logging

# logging.basicConfig(
#     level=logging.DEBUG,
#     format="%(asctime)s | %(levelname)s | "
#     "%(module)s:%(funcName)s:%(lineno)d - %(message)s",
#     datefmt="%Y-%m-%d %H:%M:%S",
#     handlers=[
#     logging.FileHandler(filename="info.log"),
#     logging.StreamHandler(),
#     ],
# )


# def main():
#     logging.debug("This is a debug message")
#     logging.info("This is an info message")
#     logging.warning("This is a warning message")
#     logging.error("This is an error message")

# if __name__ == "__main__":
#     main()

