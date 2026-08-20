import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    MAIN_URL = "https://practicum.yandex.ru/self_driving_scooter/"

    @allure.step('открываем страницу')
    def open(self):
        self.driver.get(self.MAIN_URL)

    
    @allure.step('Принимаем Куки')
    def accept_cookie(self):
        return self.click_to_element(MainPageLocators.button_cookie)


     
@allure.step('Раскрываем вопрос FAQ №{question_number}')
def click_faq_question(self, question_number: int):
    locator = (
        MainPageLocators.faq_question_form[0],
        MainPageLocators.faq_question_form[1].format(question_number)
    )
    self.click_to_element(locator)

@allure.step('Получаем текст ответа на вопрос №{answer_number}')
def get_faq_answer_text(self, answer_number: int) -> str:
    locator = (
        MainPageLocators.faq_answer_form[0],
        MainPageLocators.faq_answer_form[1].format(answer_number)
    )
    element = self.find_element_with_wait(locator)
    return element.text