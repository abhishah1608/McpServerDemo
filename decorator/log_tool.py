from functools import wraps
import logging
import sys

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
    handlers=[
        logging.FileHandler("logs/mcp.log"),
        logging.StreamHandler(sys.stderr)
    ]
)

logger = logging.getLogger("mcp")


def log_tool(func):

    @wraps(func)
    async def wrapper(*args, **kwargs):

        logger.info(f"Calling {func.__name__}")

        result = await func(*args, **kwargs)

        logger.info(f"Returned {result}")

        return result

    return wrapper