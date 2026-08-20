"""
Log filtering example from Chapter 9.
This demonstrates filtering log messages using lambda functions.
"""

from loguru import logger

logger.remove()
logger.add(
    "hello.log",
    filter=lambda record: "Hello" in record["message"],
)

def main():
    logger.info("Hello World")  # This will be logged to file
    logger.info("Bye World")    # This will NOT be logged to file
    logger.info("Hello again")  # This will be logged to file
    logger.warning("Hello warning")  # This will be logged to file
    logger.error("Goodbye error")    # This will NOT be logged to file
    
    

if __name__ == "__main__":
    main()


# import logging

# logging.basicConfig(
#     filename="hello.log", level=logging.INFO,
#     format="%(asctime)s | %(levelname)s | "
#     "%(module)s:%(funcName)s:%(lineno)d - %(message)s",
# )

# class CustomFilter(logging.Filter):
#     def filter(self, record):
#         return "Hello" in record.msg


# # Get the root logger and add the custom filter to it
# logger = logging.getLogger()
# logger.addFilter(CustomFilter())


# def main():
#     logger.info("Hello World")
#     logger.info("Bye World")


# if __name__ == "__main__":
#     main()

