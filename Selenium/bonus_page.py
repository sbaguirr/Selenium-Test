"""Selenium Test"""
from locators import BonusPageLocators

class BonusPage:
    """
    this class defines the methods for save elective courses
    """
    def __init__(self, driver):
        """
        initial method
        """
        self.driver = driver
        self.elective_course_xpath = BonusPageLocators.elective_course_xpath
        self.select_elements_xpath = BonusPageLocators.select_elements_xpath
        self.rows_xpath = BonusPageLocators.rows_xpath
        self.career_xpath = BonusPageLocators.career_xpath
        self.data_xpath = BonusPageLocators.data_xpath

    def click_elective_course(self):
        """
        This method will click on the link to display the data of the complementary courses
        """
        self.driver.find_element_by_xpath(self.elective_course_xpath).click()

    def click_100_rows(self):
        """
        This method selects the option to display 100 records so that all the
        data can be loaded and then iterated
        """
        select = self.driver.find_element_by_xpath(self.select_elements_xpath)
        for option in select.find_elements_by_tag_name('option'):
            if option.text == '100':
                option.click()
                break

    def extract_data(self):
        """
        Get data from rows
        """
        rows = self.driver.find_elements_by_xpath(self.rows_xpath)
        career_name = self.driver.find_element_by_xpath(self.career_xpath)
        data = {career_name.text: []}
        for element in rows:
            subject_code = element.find_element_by_xpath(self.data_xpath[0])
            subject_name = element.find_element_by_xpath(self.data_xpath[1])
            hours = element.find_element_by_xpath(self.data_xpath[2])
            data[career_name.text].append({
                'subject_code': subject_code.text,
                'subject': subject_name.text,
                'weekly_hours': hours.text})
        return data
