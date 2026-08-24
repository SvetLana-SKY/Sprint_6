import allure
import pytest
from conftest import driver
from pages.navigate_page import NavigatePage
from pages.main_page import MainPage




class TestLogoRedirect:
    @allure.title('Переход на главную страницу сервиса при клике на логотип "Самокат" в шапке')
    def test_logo_redirect_to_main_page_success(self, driver):
        navigate_page = NavigatePage(driver)
        main_page = MainPage(driver)
        main_page.accept_cookie()
        main_page.click_for_order_button_up()
        navigate_page.wait_visibility_of_header_logo_scooter()
        navigate_page.click_on_header_logo_scooter()
        
        assert MainPage.MAIN_URL in main_page.get_current_url()

    @allure.title('Переход на страницу "Дзена" при клике на лого "Яндекс"')
    def test_logo_redirect_to_dzen_success(self, driver):
        navigate_page = NavigatePage(driver)
        navigate_page.wait_visibility_of_header_logo_yandex()
        navigate_page.click_on_header_logo_yandex()
        navigate_page.switch_window()
        
        assert navigate_page.check_dzen_button()  