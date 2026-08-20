import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    MAIN_URL = "https://qa-scooter.praktikum-services.ru/"

    @allure.step('открываем страницу')
    def open(self):
        self.driver.get(self.MAIN_URL)

    
    @allure.step('Принимаем Куки')
    def accept_cookie(self):
        return self.click_to_element(MainPageLocators.button_cookie)

    @allure.step('Прокручиваем страницу до вопросов')
    def scroll_for_question_block(self):
        last_question_scroll = self.find_element_with_wait(MainPageLocators.last_question)
        return self.scroll_for_element(last_question_scroll)

    
    @allure.step('Кликаем на Вопрос')
    def click_for_question (self, question_id):
        question_form = self.format_locators(MainPageLocators.faq_question_form, question_id)
        self.scroll_for_question_block()
        self.click_to_element(question_form)

    @allure.step('Получение ответа на Вопрос')
    def get_answer_text(self, question_id):
        answer_text = self.format_locators(MainPageLocators.faq_answer_form, question_id)
        self.scroll_for_question_block()
        return self.get_text_from_element(answer_text)

    @allure.step('Проверяем текст ответа')
    
    def check_answer_for_question(self, question_id):
        self.click_for_question(question_id)
        return self.get_answer_text(question_id)