import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    DELAY_TIME = 20
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)
        time.sleep(15)

    def check_current_url(self):
        """
        Обновляет текущую вкладку. Выдает текущий url
        Без обновления вкладки не работает
        :return:
        url - string
        """
        self.browser.switch_to.window(self.browser.window_handles[-1])
        return self.browser.current_url

    def find_element(self, locator, timeout=DELAY_TIME):
        """
        Обновляет текущую вкладку, находит указанный в locator элемент на странице
        :param locator:
        :param timeout:
        :return:
        """
        self.browser.switch_to.window(self.browser.window_handles[-1])
        return WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator),
                                                          message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, timeout=DELAY_TIME):
        return WebDriverWait(self.browser, timeout).until(EC.presence_of_all_elements_located(locator),
                                                          message=f"Can't find elements by locator {locator}")

    def is_element_visible(self, locator, timeout=DELAY_TIME):
        try:
            WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator))
        except:
            return False
        return True

    def is_element_present(self, locator, timeout=DELAY_TIME):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator))
        except:
            return False
        return True
