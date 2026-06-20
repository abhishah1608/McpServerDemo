from server import mcpserver
from tools import tool

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


def main():
    # Initialize and run the server
    mcpserver.run(transport="stdio")
    logger.info("Server started and running.")


    

# This is what actually starts everything
if __name__ == "__main__":
    main()