import pytest
import allure
from selenium.webdriver.common.by import By
from data import CUSTOMER_1, CUSTOMER_2, RENT_1, RENT_2
from pages.order_form_page import OrderPage
from locators.main_page_locators import MainPageLocators  
from locators.order_form_locators import OrderFormLocators
from pages.main_page import MainPage

class TestOrderForm:
    @allure.step('Тестируем оформление заказа с валидными данными')
    @pytest.mark.parametrize('button', [MainPageLocators.order_button_down, MainPageLocators.order_button_up])
    @pytest.mark.parametrize("customer_data, rent_data", [(CUSTOMER_1, RENT_1), (CUSTOMER_2, RENT_2)])
    def test_created_order(self, driver,customer_data, rent_data, button):
        allure.dynamic.description(
            f"Заказ: {customer_data['name']} {customer_data['surname']}, "
            f"{rent_data['days']}. Кнопка: {'внизу' if button == MainPageLocators.order_button_down else 'вверху'}"
        )
        main_page = MainPage(driver)
       
        main_page.accept_cookie()
         
        
        main_page.created_order(button)
        order_page = OrderPage(driver)
        order_page.form_about_customer(
            name=customer_data["name"],
            surname=customer_data["surname"],
            address=customer_data["address"],
            metro=customer_data["metro"],
            phone=customer_data["phone"],
        )

        order_page.form_about_rent(
            date=rent_data["date"],
            days=rent_data["days"],
            colour=rent_data["color"],
            comment=rent_data["comment"],
        )
        order_page.click_button_order()
        order_page.confirmation_order()
        assert 'Заказ оформлен' in order_page.check_accept_order()        