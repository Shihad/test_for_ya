import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from .base_page import BasePage

class YaImgCategoryPageLocators:
    """
    Класс локаторов для страницы с открывшейся категорией
    """
    LOC_YA_IMG_CAT_SEARCH_FIELD = (By.CSS_SELECTOR, 'input.input__control')
    LOC_YA_IMG_CAT_FIRST_FOUND_PICTURE = (By.CSS_SELECTOR, 'div.serp-item_pos_0')
    LOC_YA_IMG_CAT_FIRST_FOUND_PICTURE_AFTER = (By.CSS_SELECTOR, 'a.SimpleImage-Cover')
    LOC_YA_IMG_CAT_FIRST_FOUND_PICTURE_LINK = (By.CSS_SELECTOR, 'a.Button2')
    LOCATOR_YA_IMG_CAT_OPENED_PICTURE = (By.CSS_SELECTOR, 'img.MMImage-Origin')
    LOCATOR_YA_IMG_CAT_NEXT_BUTTON = (By.CLASS_NAME, 'CircleButton_type_next')
    LOCATOR_YA_IMG_CAT_PREV_BUTTON = (By.CLASS_NAME, 'CircleButton_type_prev')
class YaImgCategoryPage(BasePage):
    """
    Страница поиска по картинкам Яндекс - открытая категория
    """
    def check_search_field(self):
        """
        Находит строку поиска и возвращает ее содержимое
        """
        search_field = (self.find_element(YaImgCategoryPageLocators.LOC_YA_IMG_CAT_SEARCH_FIELD)
                        .get_attribute("value"))
        return search_field

    def check_first_image(self):
        """
        Поскольку ссылка на оригинал изображения появляется только при наведении на картинку,
        наводим на первую картинку, чтоб она увеличилась и появилась нужная кнопка,
        находим ссылку на оригинал.
        Щелкаем, чтоб открылось окно просмотра, находим ссылку на открывшемся изображении
        :return:
        url изображения в предпросмотре, url изображения в окне просмотра - str, str
        """
        first_image = self.find_element(YaImgCategoryPageLocators.LOC_YA_IMG_CAT_FIRST_FOUND_PICTURE)
        ActionChains(self.browser).move_to_element(first_image).perform()
        time.sleep(2)
        first_image_original = self.find_element(YaImgCategoryPageLocators.LOC_YA_IMG_CAT_FIRST_FOUND_PICTURE_LINK)
        first_picture_url = first_image_original.get_property('href')
        first_image_after = self.find_element(YaImgCategoryPageLocators.LOC_YA_IMG_CAT_FIRST_FOUND_PICTURE_AFTER)
        first_image_after.click()
        time.sleep(3)
        opened_picture = self.find_element(YaImgCategoryPageLocators.LOCATOR_YA_IMG_CAT_OPENED_PICTURE)
        opened_picture_url = opened_picture.get_attribute('src')
        return first_picture_url, opened_picture_url

    def click_next_image_btn(self):
        """
        Находит и нажимает на кнопку "Следующая картинка", возвращает сгенерированный URL новой картинки.
        """
        next_btn = self.find_element(YaImgCategoryPageLocators.LOCATOR_YA_IMG_CAT_NEXT_BUTTON)
        next_btn.click()
        next_image = self.find_element(YaImgCategoryPageLocators.LOCATOR_YA_IMG_CAT_OPENED_PICTURE)
        next_image_url = next_image.get_attribute('src')
        return next_image_url

    def click_prev_image_btn(self):
        """
        Находит и нажимает на кнопку "Предыдущая картинка", возвращает сгенерированный URL старой картинки.
        """
        prev_btn = self.find_element(YaImgCategoryPageLocators.LOCATOR_YA_IMG_CAT_PREV_BUTTON)
        prev_btn.click()
        prev_image = self.find_element(YaImgCategoryPageLocators.LOCATOR_YA_IMG_CAT_OPENED_PICTURE)
        prev_image_url = prev_image.get_attribute('src')
        return prev_image_url