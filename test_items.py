import time

from selenium.webdriver.common.by import By


link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_login_link(browser):
    browser.get(link)
    button_add_to_basket = browser.find_elements(
        By.CSS_SELECTOR, ".btn-add-to-basket")
    assert button_add_to_basket, "button 'Add to basket' is not found"
    time.sleep(30)
