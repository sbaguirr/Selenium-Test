"""Selenium Test"""
from locators import EspolPageLocators


class EspolPage:
    """
    this class defines the methods for extracting data
    """
    def __init__(self, driver):
        """
        initial method
        """
        self.driver = driver
        self.faculty_list_xpath = EspolPageLocators.faculty_list_xpath
        self.ul_list_xpath = EspolPageLocators.ul_list_xpath
        self.li_list_xpath = EspolPageLocators.li_list_xpath
        self.career_link_xpath = EspolPageLocators.career_link_xpath

    def extract_data(self):
        """
        this method will extract the required data from a list with the name of the faculties
        and an unsorted list containing career data
        """
        faculty_list = self.driver.find_elements_by_xpath(self.faculty_list_xpath)
        ul_list = self.driver.find_elements_by_xpath(self.ul_list_xpath)
        # data = [['career_name_en', 'career_code', 'faculty_name', 'link_to_career_curriculum']]
        data = []
        for i, faculty in enumerate(faculty_list):
            faculty_name = faculty.text.split("\n")
            li_list = ul_list[i].find_elements_by_xpath(self.li_list_xpath)
            for li_item in li_list:
                data_li = li_item.get_attribute("textContent").replace(')', "(").split('(')
                career_name = data_li[0]
                link = li_item.find_element_by_xpath(self.career_link_xpath).get_attribute("href")
                career_code = data_li[2]
                data.append([career_name, career_code, faculty_name[1], link])
        return data


