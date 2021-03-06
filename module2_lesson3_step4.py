import math
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


options = Options()
options.add_argument("--window-position=0,0")

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")
    browser.maximize_window()

    browser.find_element_by_css_selector(".btn.btn-primary").click()
    browser.switch_to.alert().accept()

    value_of_x = browser.find_element_by_id("input_value").text
    calculated_value_of_x = calc(value_of_x)
    browser.find_element_by_class_name("form-control").send_keys(calculated_value_of_x)
    browser.find_element_by_class_name("btn-primary").click()

finally:
    time.sleep(10)
    browser.quit()
