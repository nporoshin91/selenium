import math
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--window-position=0,0")


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get(link)

    value_of_x = browser.find_element_by_id("input_value").text
    calculated_value_of_x = calc(value_of_x)
    browser.execute_script("window.scrollBy(0, 125);")
    submit_button = browser.find_element_by_tag_name("button")
    # browser.execute_script("return arguments[0].scrollIntoView(true);", submit_button)
    input_field = browser.find_element_by_id("answer")
    input_field.send_keys(calculated_value_of_x)
    browser.find_element_by_id("robotCheckbox").click()
    browser.find_element_by_id("robotsRule").click()
    submit_button.click()

finally:
    time.sleep(10)
    browser.quit()
