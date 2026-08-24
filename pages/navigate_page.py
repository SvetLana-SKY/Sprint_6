from locators.navigate_locators import NavigateLocators
from pages.base_page import BasePage
import allure

class NavigatePage(BasePage):

    @allure.step('Ждем логотип "Самокат"')
    def wait_visibility_of_header_logo_scooter(self):
        self.find_element_with_wait(NavigateLocators.header_logo_scooter)

    @allure.step('Ждем логотип "Яндекс" ')
    def wait_visibility_of_header_logo_yandex(self):
        self.find_element_with_wait(NavigateLocators.header_logo_yandex)

    @allure.step('Кликаем логотип "Самокат"')
    def click_on_header_logo_scooter(self):
        self.click_to_element(NavigateLocators.header_logo_scooter)

    @allure.step('Кликаем логотип "Яндекс"')
    def click_on_header_logo_yandex(self):
        self.click_to_element(NavigateLocators.header_logo_yandex)

    
    
    @allure.step('Находим логотип на странице Дзена')
    def check_dzen_button(self):
        return self.find_element_with_wait(NavigateLocators.logo_dzen)