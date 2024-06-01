import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
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
        
        self.driver.implicitly_wait(5)
        self.driver.get("https://www.freshworks.com/")

    def test_freshWorksLogo(self):
        flag = self.driver.find_element(By.CSS_SELECTOR, "a.logo.logo-fworks").is_displayed()
        self.assertTrue(flag)

    def test_freshWorksTitle(self):
        print("running title test...")
        title = self.driver.get_title()
        print(title)
        self.assertEqual(title, "A fresh approach to customer engagement")

    def test_getFooterLinks(self):
        footer_links_list = self.driver.find_elements(By.CSS_SELECTOR, "ul.footer-nav li a")
        for ele in footer_links_list:
            print(ele.text)
        self.assertEqual(len(footer_links_list), 35)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
