
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 20

    @allure.title('Ищем элемент на странице c таймаутом')
    def find_element_with_wait(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(locator))

    @allure.title('Кликаем по элементу, когда он станет кликабельным')
    def click_to_element(self, locator):
        element = WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable(locator))
        element.click()

    @allure.title('Получение заданного элемента')
    def get_element(self, locator):
        return self.driver.find_element(*locator)

    def add_text_to_element(self, locator, text):
        element = self.find_element_with_wait(locator)
        element.clear()
        element.send_keys(text)
        return element

    
    @allure.title('Получаем текст элемента')
    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    
    @allure.title('Пролистываем страницу до элемента')
    def scroll_for_element(self, locator):
        element = self.find_element_with_wait(locator)

        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});",
        element)  
    
        return element

  


    @allure.title('Переходим на последнюю открывшуюся вкладку')
    def switch_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.title('форматирование локатора')
    def format_locators(self, locator_1, question_id):
        method, locator = locator_1
        locator = locator.format(question_id)

        return (method, locator)

