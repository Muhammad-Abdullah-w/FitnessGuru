import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

class FreshWorksTest(unittest.TestCase):
    def setUp(self):
        browser = 'chrome'  # Change to 'firefox' to use Firefox browser
        if browser.lower() == 'chrome':
            self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        elif browser.lower() == 'firefox':
            self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        
        #self.driver.implicitly_wait(5)
        #self.driver.get("https://act7-webap.azurewebsites.net//")

    def test_freshWorksLogo(self):
        try:
            flag = self.driver.find_element(By.CSS_SELECTOR, "a.logo.logo-fworks").is_displayed()
            self.assertTrue(flag, "FreshWorks logo is not displayed on the homepage.")
        except NoSuchElementException:
            self.fail("FreshWorks logo element not found on the homepage.")

    def test_freshWorksTitle(self):
        print("running title test...")
        title = self.driver.title
        print(title)
        self.assertEqual(title, "A fresh approach to customer engagement")

    def test_getFooterLinks(self):
        # Verify if the footer contains the expected number of links
        try:
            footer_links_list = self.driver.find_elements(By.CSS_SELECTOR, "#footer a.footera")
            for ele in footer_links_list:
                print(ele.text)
            self.assertEqual(len(footer_links_list), 35, "Footer links count mismatch.")
        except NoSuchElementException:
            self.fail("Footer links not found.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
