import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--window-position=0,0")

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get(link)

    browser.find_element_by_name("firstname").send_keys("Nikolai")
    browser.find_element_by_name("lastname").send_keys("Poroshin")
    browser.find_element_by_name("email").send_keys("picknick91@gmail.com")

    file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "file.txt")

    browser.find_element_by_name("file").send_keys(file_path)
    browser.find_element_by_tag_name("button").click()

finally:
    time.sleep(10)
    browser.quit()
