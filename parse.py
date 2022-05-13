import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys

class ContextMenu(unittest.TestCase):
    ###ContextMenu###
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = "http://the-internet.herokuapp.com/context_menu"
        self.driver.maximize_window()
        time.sleep(5)
        self.driver.get(self.base_url)
        time.sleep(2)

    def test_ContextMenu(self):
        driver = self.driver
        self.assertIn(self.base_url, driver.current_url)

        menu = driver.find_element(By.ID, "hot-spot")
        self.assertTrue(menu)
        actions = ActionChains(driver)
        actions.context_click(menu)
        time.sleep(2)
        driver.save_screenshot("Click.png")
        time.sleep(5)


        actions.perform()
        time.sleep(2)

        alert = driver.switch_to.alert
        alert.accept()
        time.sleep(5)
        driver.save_screenshot("Enter.png")

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()


