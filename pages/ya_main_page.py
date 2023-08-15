import time
from selenium.webdriver.common.by import By

from .base_page import BasePage

class YaMainPageLocators:
    LOC_YA_BODY = (By.TAG_NAME,"body")
    LOC_YA_SEARCH_FIELD = (By.ID, "text")
    LOC_YA_SUGGEST_LIST = (By.CSS_SELECTOR, ".mini-suggest__popup-content")
    LOC_YA_SEARCH_BUTTON = (By.CLASS_NAME, "search3__button")
    LOC_YA_NAV_BAR = (By.CSS_SELECTOR, ".HeaderDesktopNavigation")
    LOC_YA_ALL_MENU_BUTTON = (By.CLASS_NAME, "services-suggest__icons-more")
    LOC_YA_IMAGES_BUTTON = (By.CSS_SELECTOR, 'a[href="https://ya.ru/images/"]')

class YaMainPage(BasePage):

    def enter_word(self, word):
        search_field = self.find_element(YaMainPageLocators.LOC_YA_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        time.sleep(10)
        return search_field

    def check_suggest_list_visibility(self):
        return self.is_element_visible(YaMainPageLocators.LOC_YA_SUGGEST_LIST)

    def check_open(self):
        return self.is_element_present(YaMainPageLocators.LOC_YA_BODY)

    def check_all_menu_button(self):
        return self.is_element_visible(YaMainPageLocators.LOC_YA_ALL_MENU_BUTTON)

    def check_images_button(self):
        return self.is_element_visible(YaMainPageLocators.LOC_YA_IMAGES_BUTTON)

    def click_on_the_all_menu_button(self):
        return self.find_element(YaMainPageLocators.LOC_YA_ALL_MENU_BUTTON, timeout=2).click()

    def click_on_the_search_button(self):
        return self.find_element(YaMainPageLocators.LOC_YA_SEARCH_BUTTON, timeout=2).click()

    def click_on_the_images_button(self):
        return self.find_element(YaMainPageLocators.LOC_YA_IMAGES_BUTTON, timeout=2).click()