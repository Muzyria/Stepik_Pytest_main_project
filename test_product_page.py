from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)  # инициализируем
    page.open()                        # открываем страницу
    page.click_button_add_to_bucket()  # Нажимаем на кнопку "Добавить в корзину"
    page.solve_quiz_and_get_code()     # Посчитать результат математического выражения и ввести ответ
    page.should_be_message_about_adding()  # Название товара в сообщении должно совпадать с тем товаром, который вы действительно добавили.
    page.should_be_message_basket_total()  # Сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара
