import os
import sys
sys.path.append(os.getcwd())
from utils.common_imports import *

if not os.path.exists('logs'):
    os.makedirs('logs')

file_name = Path("logs") / f"log_file.log"

log.basicConfig(
    filename=file_name,
    level=log.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%d-%m-%Y %H:%M:%S"
)

logg = log.getLogger()

def log_info(msg):
    logg.info(msg,stack_info=False)

def log_error(msg):
    logg.error(msg,stack_info=False)

def log_critical(msg):
    logg.critical(msg,stack_info=False)

