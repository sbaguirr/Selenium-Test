import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class EspolSearch(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='Drivers\\chromedriver.exe')

    def test_search_in_espol(self):
        driver = self.driver
        driver.get("http://www.espol.edu.ec/es/educacion/grado/catalogo")
        list_faculty = driver.find_elements_by_xpath("//div[@id='accordion']/div/div/h4/a/strong")
        list_ul = driver.find_elements_by_xpath("//div[@class='panel-body']/ul[2]")
        for i in range(len(list_faculty)):
            faculty_name = list_faculty[i].text.split("\n")
            print(faculty_name[1])
            list_li = list_ul[i].find_elements_by_xpath(".//li")
            for li in list_li:
                link_career = li.find_element_by_xpath(".//a").get_attribute("href")
                code_career = li.find_element_by_xpath(".//span").get_attribute("textContent")
                name_career = li.text
                print(name_career)
                print(link_career)
                print(code_career)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
