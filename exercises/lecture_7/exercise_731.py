import logging


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)-8s | %(module)-10s: %(funcName)-4s | %(message)s",
    handlers=[
        logging.FileHandler("logfile.log", encoding="utf-8"),
        logging.StreamHandler(),
    ],
)

logger = logging.getLogger(__name__)


def add(a: float, b: float) -> float:
    logger.info(f"Calculating: {a} + {b}")

    if type(a) != int:
        logger.error("A is not an int")
        return None
    if type(b) != int:
        logger.error("B is not an int")
        return None

    result = a + b
    logger.info(f"Found result: {result}")
    return result


def sub(a: float, b: float) -> float:
    logger.info(f"Calculating: {a} - {b}")

    if type(a) != int:
        logger.error("A is not an int")
        return None
    if type(b) != int:
        logger.error("B is not an int")
        return None

    result = a - b
    logger.info(f"Found result: {result}")
    return result


def main():
    logger.info("Main programm running")

    a = 10
    b = 5
    c = "20"

    result = add(a, b)
    logger.info(f"Result: {a} + {b} = {result}")

    result = sub(a, b)
    logger.info(f"Result: {a} - {b} = {result}")

    result = sub(a, c)
    logger.info(f"Result: {a} - {c} = {result}")


if __name__ == "__main__":
    main()
