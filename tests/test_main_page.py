import allure
import pytest

from data import answer_for_question
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage


class TestsMainPage:
    @allure.title('Проверяем выпадающий список вопросы-ответы')
    @pytest.mark.parametrize("question_id, expected_answer", answer_for_question.items())
    def test_check_answer_for_question(self, driver, question_id, expected_answer):
        main_page = MainPage(driver)
        main_page.accept_cookie()
        main_page.scroll_for_question_block()
        assert main_page.check_answer_for_question(question_id) == expected_answer