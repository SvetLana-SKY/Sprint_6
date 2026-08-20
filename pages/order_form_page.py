import allure

from selenium.webdriver.common.by import By
from data import CUSTOMER_1, CUSTOMER_2, RENT_1, RENT_2
from locators.order_form_locators import OrderFormLocators
from pages.base_page import BasePage

class OrderPage(BasePage):

    @allure.step('Заполняем поле Имя')
    def input_name(self, name):
        return self.add_text_to_element(OrderFormLocators.placeholder_name, name)

    @allure.step('Заполняем поле Фамилия')
    def input_surname(self, surname):
        return self.add_text_to_element(OrderFormLocators.placeholder_surname, surname)

    @allure.step('Заполняем поле Адресс')
    def input_address(self, address):
        return self.add_text_to_element(OrderFormLocators.placeholder_address, address)

    @allure.step('Заполняем поле Метро')
    def input_metro(self, metro):
        return self.add_text_to_element(OrderFormLocators.placeholder_metro, metro)

    
    @allure.step('Заполняем поле Телефон')
    def input_phone(self, phone):
        return self.add_text_to_element(OrderFormLocators.placeholder_phone, phone)

    @allure.step('Заполняем Форму Для кого самокат')
    def form_about_customer(self, name, surname, address, metro, phone):
        self.input_name(name)
        self.input_surname(surname)
        self.input_address(address)
        self.input_metro(metro)
        self.input_phone(phone)
        self.click_to_element(OrderFormLocators.button_next)

    @allure.step('Заполняем поле Дата')
    def input_date_rent(self, date):
        return self.add_text_to_element(OrderFormLocators.placeholder_date_rent, date)


    @allure.step('Заполняем поле Срок аренды')
    def set_days(self, days):
        self.click_to_element(OrderFormLocators.placeholder_count_rent_day)

        locator_for_day = OrderFormLocators.list_count_rent_day.format(days)
        self.click_to_element((By.XPATH, locator_for_day))

    @allure.step('Заполняем цвет')
    def checkbox_colour(self, colour):
        scooter_colour = self.format_locators(OrderFormLocators.checkbox_colour, colour)
        return self.click_to_element(scooter_colour)  

    @allure.step('Заполняем поле Комментарий')
    def comment_input(self,comment):
        return self.add_text_to_element(OrderFormLocators.input_comment, comment)      

    @allure.step('Заполняем форму Про аренду')
    def form_about_rent(self,date, days, colour, comment):
        self.input_date_rent(date)
        self.set_days(days)
        self.checkbox_colour(colour)
        self.comment_input(comment)

    @allure.step('Нажимаем на кнопку заказать в форме')
    def click_button_order(self):
        self.click_to_element(OrderFormLocators.button_order)

    @allure.step('Подтверждаем заказ')
    def confirmation_order(self):
        self.click_to_element(OrderFormLocators.button_order_confirmation)

    @allure.step('Получаем подтверждение об оформленном заказе')
    def check_accept_order(self):
        return self.get_text_from_element(OrderFormLocators.title_order_add)   


    