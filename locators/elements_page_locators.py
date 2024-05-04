from selenium.webdriver.common.by import By


class TextBoxPageLocators:

    FULL_NAME = (By.XPATH, '//*[@id = "userName"]')
    EMAIL = (By.CSS_SELECTOR, 'input[id="userEmail"]')
    CURRENT_ADDRESS = (By.CSS_SELECTOR , 'textarea[id="currentAddress"]')
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, 'textarea[id="permanentAddress"]')
    SUBMIT = (By.CSS_SELECTOR, 'button[id="submit"]')


    CREATED_FULL_NAME = (By.CSS_SELECTOR, 'p[id="name"]')
    CREATED_EMAIL = (By.CSS_SELECTOR, 'p[id="email"]')
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, 'p[id="currentAddress"]')
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, 'p[id="permanentAddress"]')



class CheckBoxPageLocators:

    EXPAND_ALL_BUTTON = (By.XPATH, '//*[@title = "Expand all"]')
    ITEM_LIST = (By.XPATH, '//*[@class ="rct-title"]')
    CHECKED_ITEMS = (By.CSS_SELECTOR, 'svg[class="rct-icon rct-icon-check"]')
    TITLE_ITEM = './/ancestor::span[@class="rct-text"]'
    OUTPUT_RESULT = (By.CSS_SELECTOR, 'span[class="text-success"]')