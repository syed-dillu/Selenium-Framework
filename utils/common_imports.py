from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.remote.webelement import WebElement
from pathlib import Path
import time
import logging as log
from dotenv import load_dotenv

from datetime import datetime
from typing import Union, Optional
import pytest
import allure
import os
from allure_commons.types import AttachmentType
import pandas as pd


dir = Path(os.getcwd())

