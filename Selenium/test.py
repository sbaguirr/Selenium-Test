import unittest
from Selenium.espolPage import EspolPage
from selenium import webdriver


class EspolSearch(unittest.TestCase):
    """Test class to extract data in ESPOL'S website"""
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='Drivers\\chromedriver.exe')
        self.driver.get("http://www.espol.edu.ec/es/educacion/grado/catalogo")

    def test_extract_data(self):
        page = EspolPage(self.driver)
        page.extract_data()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
