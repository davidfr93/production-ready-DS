import logging


# logging.basicConfig(
#     level=logging.DEBUG,
#     format="%(asctime)s | %(levelname)s | "
#     "%(module)s:%(funcName)s:%(lineno)d - %(message)s",
#     datefmt="%Y-%m-%d %H:%M:%S",
# )




logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | "
    "%(module)s:%(funcName)s:%(lineno)d - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


def main():
    logging.debug("Loaded 1000 rows")
    logging.info("Training RandomForest model")
    logging.warning("Missing values detected")
    logging.error("Model training failed")

if __name__ == "__main__":
    main()


























