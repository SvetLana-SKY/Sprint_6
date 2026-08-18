from selenium.webdriver.common.by import By

class MainPageLocators:
    order_button_up = By.XPATH, '//div[@class="Header_Nav__AGCXC"]/button[@class="Button_Button__ra12g" and text()="Заказать"]'
    order_button_down = By.XPATH, '//button[contains(@class, "Button_Middle") and text() = "Заказать"]'
    button_cookie = By.ID, 'rcc-confirm-button'
    faq_question_form = By.XPATH, '//div[@id="accordion__heading-{}"]'
    faq_answer_form = By.XPATH, '//div[@id="accordion__panel-{}"]/p'
    last_question = By.XPATH, '//div[@id="accordion__heading-7"]'