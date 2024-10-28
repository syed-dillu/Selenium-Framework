import os
import sys

sys.path.append(os.getcwd())
from utils.common_imports import *
load_dotenv()

config : dict[str,str] = {
    "URL" : os.getenv("BASE_URL","https://demo.guru99.com/test/newtours/register.php"),
    "USERNAME" : os.getenv("USER_NAME","syed@gmail.com"),
    "PASSWORD" : os.getenv("PASS_WORD","syed@123"),
    "EXPLICIT_TIME" : 20,
    "TIME_OUT" : 20,
    "TEST_DATA"  :  dir / "data" / "test_data.xlsx"
}


def get_url() -> str:
    return config["URL"]

def get_username() -> str:
    return config["USERNAME"]

def get_password() -> str:
    return config["PASSWORD"]

def get_expilicitwait() -> int :
    return config["EXPLICIT_TIME"]

def get_time_out() -> int :
    return config["TIME_OUT"]

def get_testdata_url() -> str :
    return config["TEST_DATA"]


if __name__ == "__main__":
    url = get_url()
    print(f"URL : {url}")