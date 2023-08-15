from selenium.webdriver.common.by import By

from .base_page import BasePage

class YaSearchResPageLocators:
    LOC_YA_RESULT_LIST = (By.CSS_SELECTOR, "#search-result")
    LOC_YA_RESULT_HREFS = (By.CSS_SELECTOR, "#search-result a")

class YaSearchResultPage(BasePage):
    def check_result_list_presence(self):
        return self.is_element_present(YaSearchResPageLocators.LOC_YA_RESULT_LIST)

    def check_first_result(self):
        hrefs = self.find_elements(YaSearchResPageLocators.LOC_YA_RESULT_HREFS)
        first_href=hrefs[0].get_attribute("href")
        return first_href
