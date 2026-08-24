from selenium.webdriver.common.by import By

class NavigateLocators:
    
    header_logo_scooter = (By.XPATH, '//a[@href="/" and contains(@class, "Header_LogoScooter")]')
    header_logo_yandex = (By.XPATH, '//a[@href="//yandex.ru" and contains(@class, "Header_LogoYandex")]')
    title_of_page = (By.TAG_NAME, 'title')
    logo_dzen = By.XPATH, '//*[contains(@class, "header__logoLink")]'