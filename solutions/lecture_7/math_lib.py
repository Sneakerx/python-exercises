"""This module contains basic mathematical operations."""

import logging

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
