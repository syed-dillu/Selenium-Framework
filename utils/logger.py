from pathlib import Path
import logging
from logging.handlers import RotatingFileHandler

log_dir = Path("logs")
log_dir.mkdir(exist_ok=True)

log_file = log_dir / "log_data.log"

logger = logging.getLogger("custome-logger")
logger.setLevel(level=logging.DEBUG)

file_handler = RotatingFileHandler(log_file)
console_handler = logging.StreamHandler()

logger.addHandler(file_handler)
logger.addHandler(console_handler)

formatter = logging.Formatter(
    fmt= "%(asctime)s - %(levelname)s - %(message)s",
    datefmt= "%d-%m-%Y %H:%M:%S"
)

file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

def log_info(msg):
    logger.info(msg)

def log_error(msg):
    logger.error(msg)

