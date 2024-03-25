
import pytest

from pages.product_page import ProductPage


@pytest.mark.smoke
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)      # инициализируем
    page.open()                            # открываем страницу
    page.should_not_be_success_message()   # ожидаем, что там нет сообщения об успешном добавлении в корзину
    page.click_button_add_to_bucket()      # Нажимаем на кнопку "Добавить в корзину"
    page.solve_quiz_and_get_code()         # Посчитать результат математического выражения и ввести ответ
    page.should_be_message_about_adding()  # Название товара в сообщении должно совпадать с тем товаром, который вы действительно добавили.
    page.should_be_message_basket_total()  # Сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара


@pytest.mark.need_review
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"])
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    """ Открываем страницу товара
        Добавляем товар в корзину
        Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    """
    page = ProductPage(browser, link)       # инициализируем
    page.open()                             # открываем страницу
    page.click_button_add_to_bucket()       # Нажимаем на кнопку "Добавить в корзину"
    page.solve_quiz_and_get_code()          # Посчитать результат математического выражения и ввести ответ
    page.should_not_be_success_message()    # Проверяем, что нет сообщения


@pytest.mark.need_review
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"])
def test_guest_cant_see_success_message(browser, link):
    """
        Открываем страницу товара
        Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    """
    page = ProductPage(browser, link)     # инициализируем
    page.open()                           # открываем страницу
    page.should_not_be_success_message()  # Проверяем, что нет сообщения


@pytest.mark.need_review
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"])
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    """
        Открываем страницу товара
        Добавляем товар в корзину
        Проверяем, что нет сообщения об успехе с помощью is_disappeared:
    """
    page = ProductPage(browser, link)  # инициализируем
    page.open()                        # открываем страницу
    page.click_button_add_to_bucket()  # Нажимаем на кнопку "Добавить в корзину"
    page.solve_quiz_and_get_code()     # Посчитать результат математического выражения и ввести ответ
    page.should_is_disappeared()       # Проверяем, что нет сообщения об успехе с помощью is_disappeared
