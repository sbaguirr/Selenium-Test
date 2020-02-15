import unittest
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class EspolSearch(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='Drivers\\chromedriver.exe')

    def test_search_in_espol(self):
        driver = self.driver
        driver.get("http://www.espol.edu.ec/es/educacion/grado/catalogo")
        faculty_list = driver.find_elements_by_xpath("//div[@id='accordion']/div/div/h4/a/strong")
        ul_list = driver.find_elements_by_xpath("//div[@class='panel-body']/ul[2]")
        data = [['career_name_en','career_code','faculty_name','link_to_career_curriculum']]
        for i in range(len(faculty_list)):
            faculty_name = faculty_list[i].text.split("\n")
            li_list = ul_list[i].find_elements_by_xpath(".//li")
            for li in li_list:
                career_link = li.find_element_by_xpath(".//a").get_attribute("href")
                career_code = li.find_element_by_xpath(".//span").get_attribute("textContent")
                career_name = li.text
                data.append([career_name, career_code, faculty_name[1], career_link])

        file = open('data.csv', 'w')
        with file:
            writer = csv.writer(file)
            writer.writerows(data)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
