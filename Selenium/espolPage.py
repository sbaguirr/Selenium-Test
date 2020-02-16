import csv
from Selenium.locators import EspolPageLocators


class EspolPage:
    def __init__(self, driver):
        """ Base class to initialize the base page that will be called from all pages"""
        self.driver = driver
        self.faculty_list_xpath = EspolPageLocators.faculty_list_xpath
        self.ul_list_xpath = EspolPageLocators.ul_list_xpath
        self.li_list_xpath = EspolPageLocators.li_list_xpath
        self.career_link_xpath = EspolPageLocators.career_link_xpath

    def extract_data(self):
        faculty_list = self.driver.find_elements_by_xpath(self.faculty_list_xpath)
        ul_list = self.driver.find_elements_by_xpath(self.ul_list_xpath)
        data = [['career_name_en', 'career_code', 'faculty_name', 'link_to_career_curriculum']]
        for i in range(len(faculty_list)):
            faculty_name = faculty_list[i].text.split("\n")
            li_list = ul_list[i].find_elements_by_xpath(self.li_list_xpath)
            for li in li_list:
                career_name_code = li.get_attribute("textContent").replace(')', "(").split('(')
                career_link = li.find_element_by_xpath(self.career_link_xpath).get_attribute("href")
                data.append([career_name_code[0], career_name_code[2], faculty_name[1], career_link])
        self.save_csv(data)

    @staticmethod
    def save_csv(data):
        file = open('data.csv', 'w', encoding="utf-8")
        with file:
            writer = csv.writer(file)
            writer.writerows(data)
