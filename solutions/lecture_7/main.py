import logging
import math_lib

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)-8s | %(module)-10s: %(funcName)-4s | %(message)s",
)

logger = logging.getLogger(__name__)


def main():
    logger.info("Main programm running")

    a = 10
    b = 5
    c = "20"

    result = math_lib.add(a, b)
    logger.info(f"Result: {a} + {b} = {result}")

    result = math_lib.sub(a, b)
    logger.info(f"Result: {a} - {b} = {result}")

    result = math_lib.sub(a, c)
    logger.info(f"Result: {a} - {c} = {result}")


if __name__ == "__main__":
    main()
