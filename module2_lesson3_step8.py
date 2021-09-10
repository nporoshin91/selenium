import math
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


options = Options()
options.add_argument("--window-position=0,0")

try:

    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    browser.maximize_window()

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    button = WebDriverWait(browser, 12).until(ec.text_to_be_present_in_element((By.ID, "price"), "$100"))
    # говорим Selenium проверять в течение 5 секунд пока кнопка станет неактивной
    # button = WebDriverWait(browser, 5).until_not(ec.element_to_be_clickable((By.ID, "verify")))
    browser.find_element_by_id("book").click()

    value_of_x = browser.find_element_by_id("input_value").text
    calculated_value_of_x = calc(value_of_x)
    browser.find_element_by_class_name("form-control").send_keys(calculated_value_of_x)
    browser.find_element_by_id("solve").click()

finally:
    time.sleep(10)
    browser.quit()
