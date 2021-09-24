import math
import time

import pytest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

options = Options()
options.add_argument("--window-position=0,0")


@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome(options=options)
    browser.maximize_window()
    yield browser
    print("\nquit browser..")
    browser.quit()


links = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
]

sentence = ""


@pytest.mark.parametrize("link", links)
def test_guest_should_see_login_link(browser, link):
    browser.get(link)
    WebDriverWait(browser, 5).until(
        ec.visibility_of_element_located((By.CSS_SELECTOR, ".textarea"))).send_keys(str(math.log(int(time.time()))))
    browser.find_element_by_css_selector(".submit-submission").click()
    try:
        assert WebDriverWait(browser, 3).until(
            ec.text_to_be_present_in_element((By.CSS_SELECTOR, ".smart-hints__hint"), "Correct!"))
    except:
        global sentence
        sentence += browser.find_element_by_css_selector(".smart-hints__hint").text
        print(f"\n{sentence}")
