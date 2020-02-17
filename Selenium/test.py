"""Selenium Test"""
import unittest
import time
from selenium import webdriver
from bonus_page import BonusPage
from espol_page import EspolPage
from file import File


class EspolSearch(unittest.TestCase):
    """
    Test class to extract data in ESPOL'S website
    """
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='Drivers\\chromedriver.exe')
        self.driver.get("http://www.espol.edu.ec/es/educacion/grado/catalogo")

    def test_extract_data(self):
        """
        This method calls the function that extracts data
        File.save_csv(data, "data")
        """
        page = EspolPage(self.driver)
        data = page.extract_data()
        File.save_csv(data)
        # Bonus
        big_data = {'ElectiveCourse': []}
        for element in data:
            self.driver.get(element[3])
            new_page = BonusPage(self.driver)
            new_page.click_elective_course()
            new_page.click_100_rows()
            time.sleep(15)   # is necessary to avoid exceptions while the page is loading
            big_data['ElectiveCourse'].append(new_page.extract_data())
        File.save_json(big_data)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
