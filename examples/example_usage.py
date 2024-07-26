from custom_logging import CustomLogger
from dotenv import load_dotenv

load_dotenv()

def main():
    logger = CustomLogger('mylogger')
    logger.trace("This is a trace log message")
    logger.debug("This is a debug log message")
    logger.info("This is an info log message")
    logger.warn("This is a warning log message")
    logger.error("This is an error log message")
    logger.critical("This is a critical log message")

if __name__ == "__main__":
    main()