import os
import sys
sys.path.append(os.getcwd())
from utils.common_imports import *
from utils.selenium_helpers import SeleniumHelper
from utils.logger import log_info


class KabukaTable(SeleniumHelper):

    TABLE = (By.TAG_NAME,"table")
    TABLE_ROW = (By.TAG_NAME,"tr")
    TABLE_CELL = (By.TAG_NAME,"td")
    ALL_ELEMENT = (By.XPATH,"//table//tbody//tr//td")


    def table(self):
        table = self.get_element(*self.TABLE)
        self.driver.execute_script("arguments[0].scrollIntoView()",table)
        tr = table.find_elements(*self.TABLE_ROW)
        data = []
        for row in tr:
            cells = row.find_elements(*self.TABLE_CELL)
            for cell in cells:
                data.append(cell.text)
        print(data , "\n")
    
    def all_data(self):
        all = self.get_elements(*self.ALL_ELEMENT)
        all_data = []
        for data in all:
            all_data.append(data.text)
        print(all_data)    

if __name__ == "__main__":
    k = KabukaTable(driver=webdriver.Chrome())
    k.site_url("https://www.kapruka.com/online/samedaydelivery")
    k.table()
    k.all_data()

