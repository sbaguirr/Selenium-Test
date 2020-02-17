"""Selenium Test"""


class EspolPageLocators:
    """
     Class for Espol page locators.
    """
    faculty_list_xpath = "//div[@id='accordion']/div/div/h4/a/strong"
    ul_list_xpath = "//div[@class='panel-body']/ul[2]"
    li_list_xpath = ".//li"
    career_link_xpath = ".//a"


class BonusPageLocators:
    """
     Class for Bonus page locators.
    """
    elective_course_xpath = "//p[@id='informacion']/a"
    select_elements_xpath = "//select[@name='tbl_materias_complementarias_length']"
    rows_xpath = "//table[@id='tbl_materias_complementarias']/tbody/tr"
    career_xpath = "//h1"
    data_xpath = [".//td[1]", ".//td[2]", ".//td[3]"]
