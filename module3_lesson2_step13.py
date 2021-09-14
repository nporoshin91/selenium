import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--window-position=0,0")


class TestRegistration(unittest.TestCase):
    def test_Registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome(options=options)
        browser.maximize_window()
        browser.get(link)
        fname = browser.find_element_by_css_selector(".form-control.first")
        fname.send_keys("Ivan")
        lname = browser.find_element_by_css_selector(".form-control.second")
        lname.send_keys("Petrov")
        email = browser.find_element_by_css_selector(".form-control.third")
        email.send_keys("email@domain.com")
        phone = browser.find_element_by_xpath("//div[@class='second_block']//input[@class='form-control first']")
        phone.send_keys("+375447654321")
        address = browser.find_element_by_xpath("//div[@class='second_block']//input[@class='form-control second']")
        address.send_keys("Smolensk")
        button = browser.find_element_by_xpath("//button[@type='submit']")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
        browser.quit()

    def test_Registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.maximize_window()
        browser.get(link)
        first_name = browser.find_element_by_css_selector(".first_block .form-control.first")
        first_name.send_keys("Starcraft: Broodwar")
        last_name = browser.find_element_by_css_selector(".first_block .form-control.second")
        last_name.send_keys("Starcraft: Broodwar")
        email = browser.find_element_by_css_selector(".first_block .form-control.third")
        email.send_keys("Starcraft: Broodwar")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
        browser.quit()


if __name__ == "__main__":
    unittest.main()
