from selenium.webdriver.common.by import By

class OrderFormLocators:

    # информация о заказчике
    order_form = By.XPATH, '//div[text()="Для кого самокат"]'
    placeholder_name = By.XPATH, '//input[@placeholder="* Имя"]'
    placeholder_surname = By.XPATH, '//input[@placeholder="* Фамилия"]'
    placeholder_address = By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]'
    placeholder_phone = By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]'
    placeholder_metro = By.XPATH, '//input[@placeholder = "* Станция метро"]'
    button_next = By.XPATH, '//button[text()="Далее"]'

    # информация об аренде
    order_rent = By.XPATH, '//div[text()="Про аренду"]'
    placeholder_date_rent = By.XPATH, '//input[@placeholder = "* Когда привезти самокат"]'
    calendar_date = By.XPATH, '//*[contains(@class, "react-datepicker__day") and text()="{}"]'
    placeholder_count_rent_day = By.XPATH, '//div[@class="Dropdown-placeholder" and text()="* Срок аренды"]'
    list_count_rent_day = By.XPATH, '//div[@class="Dropdown-option" and text()="{}"]'
    checkbox_colour = By.XPATH, '//*[@id="{}"]'
    placeholder_comment = By.XPATH, '//input[@placeholder = "Комментарий для курьера"]'
    button_back = By.XPATH, '//button[text()="Назад"]'
    button_order = By.XPATH, '//button[contains(@class, "Button_Middle") and text()="Заказать"]'

    # всплывающие окна
    title_order_confirmation = By.XPATH, '//div[text()="Хотите оформить заказ?"]'
    button_order_confirmation = By.XPATH, '//button[text()="Да"]'
    title_order_add = By.XPATH, '//div[text()="Заказ оформлен"]'