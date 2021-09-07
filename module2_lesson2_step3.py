import math
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

options = Options()
options.add_argument("--window-position=0,0")


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get(link)

    value1 = browser.find_element_by_id("num1").text
    value2 = browser.find_element_by_id("num2").text
    sum_of_values = int(value1) + int(value2)
    dropdown = browser.find_element_by_tag_name("select")
    Select(dropdown).select_by_value(str(sum_of_values))
    browser.find_element_by_tag_name("button").click()

finally:
    time.sleep(10)
    browser.quit()
