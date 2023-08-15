from selenium.webdriver.common.by import By

from .base_page import BasePage

class YaSearchImgPageLocators:
    YA_IMG_URL = "https://ya.ru/images/"
    LOC_YA_IMG_LIST = (By.CSS_SELECTOR, "#search-result")
    LOC_YA_IMG_HREFS = (By.CSS_SELECTOR, "div .PopularRequestList-SearchText")

class YaSearchImgPage(BasePage):

    def check_img_url(self):
        return self.check_current_url()

    def check_first_category_text_and_click(self):
        categories = self.find_elements(YaSearchImgPageLocators.LOC_YA_IMG_HREFS)
        first_category = categories[0]
        return first_category.click(), first_category.text


    def check_result_list_presence(self):
        assert self.is_element_present(YaSearchResPageLocators.LOC_YA_RESULT_LIST), "Result list can't be found"


