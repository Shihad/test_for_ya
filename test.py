import time

from pages.ya_main_page import YaMainPage
from pages.ya_search_result_page import YaSearchResultPage
from pages.ya_search_images_page import YaSearchImgPage
from pages.ya_images_category_page import YaImgCategoryPage

def test_yandex_search(browser):
    """
    Проверка работы поисковой системы.
    1.Открываем страницу "ya.ru"
    2.Вводим в поисковую строку слово "Тензор"
    3.Проверяем видимость списка подсказок.
    4.Щелкаем на кнопку поиска
    5.В открывшемся окне проверяем, что есть список результатов поиска
    6.Проверяем, что первая ссылка ведет на tensor.ru
    :param browser:
    :return:
    """
    yandex_main_page = YaMainPage(browser, "https://ya.ru")
    yandex_main_page.open()
    ya_main_page_opened = yandex_main_page.check_open()
    assert ya_main_page_opened, "Ya.ru Page hasn't opened properly. Check antirobot defence"
    yandex_main_page.enter_word("Тензор")
    ya_main_page_suggest_visible = yandex_main_page.check_suggest_list_visibility()
    assert ya_main_page_suggest_visible, "Suggest list is invisible"
    yandex_main_page.click_on_the_search_button()
    yandex_result_page = YaSearchResultPage(browser, browser.current_url)
    #Добавлено на работу антироботовой защиты яндекса
    time.sleep(20)
    ya_res_page_results_present = yandex_result_page.check_result_list_presence()
    assert ya_res_page_results_present, "Result list can't be found"
    ya_res_page_first_url = yandex_result_page.check_first_result()
    target_url = "tensor.ru"
    assert target_url in ya_res_page_first_url, f"{target_url} isn't first result"

def test_yandex_picture_search(browser):
    """
    Проверка работы поиска по картинкам
    1.Открываем страницу "ya.ru" и проверяем это
    2.Вводим в поисковую строку слово "Поиск по картинкам", чтоб появились панели меню
    3.Проверяем видимость кнопки "Все" и кликаем по ней.
    4.Проверяем наличие кнопки "Картинки" и кликаем по ней
    5.В открывшемся окне проверяем url, открылась ли нужная страница
    6.Проверяем наличие первой категории, запоминаем её и щелкаем по ней
    7.В открывшемся окне проверяем совпадение текста строки поиска с названием категории
    8.Находим ссылку на первом изображении, щелкаем по первому изображению и находим ссылку на открывшееся
    9.Проверяем работу кнопки "вперед" - при нажатии url открытой картинки меняется
    10.Проверяем работу кнопки "назад" - при нажатии url открытой картинки возвращается к исходному
    :param browser:
    :return:
    """
    YA_IMG_URL = "https://ya.ru/images/"
    yandex_main_page = YaMainPage(browser, "https://ya.ru")
    yandex_main_page.open()
    ya_main_page_opened = yandex_main_page.check_open()
    assert ya_main_page_opened, "Ya.ru Page hasn't opened properly. Check antirobot defence"
    yandex_main_page.enter_word("Поиск по картинкам")
    ya_main_page_all_menu_visible = yandex_main_page.check_all_menu_button()
    assert ya_main_page_all_menu_visible, "Menu button is invisible"
    yandex_main_page.click_on_the_all_menu_button()
    ya_main_page_images_visible=yandex_main_page.check_images_button()
    assert ya_main_page_images_visible, "Images button is invisible"
    yandex_main_page.click_on_the_images_button()
    # Добавлено на работу антироботовой защиты яндекса
    time.sleep(15)
    yandex_img_page = YaSearchImgPage(browser, browser.current_url)
    # Добавлено на работу антироботовой защиты яндекса
    time.sleep(20)
    ya_img_page_url = yandex_img_page.check_img_url()
    assert ya_img_page_url == YA_IMG_URL, f"{YA_IMG_URL} cant't be loaded"
    _, first_category = yandex_img_page.check_first_category_text_and_click()
    # Добавлено на работу антироботовой защиты яндекса
    time.sleep(12)
    yandex_img_category_page =YaImgCategoryPage(browser, browser.current_url)
    # Добавлено на работу антироботовой защиты яндекса
    time.sleep(10)
    search_field_text = yandex_img_category_page.check_search_field()
    assert search_field_text == first_category, "Opened category not in search field"
    # Добавлено на работу антироботовой защиты яндекса
    time.sleep(20)
    origin_image_url, opened_image_url = yandex_img_category_page.check_first_image()
    assert origin_image_url == opened_image_url, "Opened image isn't equal selected one"
    opened_image_url = yandex_img_category_page.click_next_image_btn()
    assert not origin_image_url == opened_image_url, 'Image did not change'
    opened_image_url = yandex_img_category_page.click_prev_image_btn()
    assert origin_image_url == opened_image_url, 'Current image is not previous one'
