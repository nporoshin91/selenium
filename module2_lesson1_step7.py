import math
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--window-position=0,0")


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get(link)

    hidden_value_of_x = browser.find_element_by_id("treasure").get_attribute("valuex")
    calculated_value_of_hidden_x = calc(hidden_value_of_x)
    browser.find_element_by_id("answer").send_keys(calculated_value_of_hidden_x)
    browser.find_element_by_id("robotCheckbox").click()
    browser.find_element_by_id("robotsRule").click()
    browser.find_element_by_css_selector("button.btn").click()

finally:
    time.sleep(10)
    browser.quit()
