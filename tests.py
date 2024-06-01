import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

class CultFitTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run headless Chrome
        chrome_service = Service('path_to_chromedriver')
        cls.driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
        cls.driver.get("https://act7-webap.azurewebsites.net/")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_page_title(self):
        self.assertEqual(self.driver.title, "Get Fitness Workouts, Gyms, Health Care, & Healthy Food in India by Cult.fit")

    def test_navbar_presence(self):
        navbar = self.driver.find_element(By.ID, "navbar")
        self.assertTrue(navbar.is_displayed())

    def test_video_autoplay(self):
        video = self.driver.find_element(By.TAG_NAME, "video")
        autoplay = video.get_attribute("autoplay")
        self.assertIsNotNone(autoplay)
        self.assertEqual(autoplay, "")

    def test_footer_links(self):
        footer_links = self.driver.find_elements(By.CLASS_NAME, "footera")
        for link in footer_links:
            self.assertTrue(link.is_displayed())
            self.assertEqual(link.value_of_css_property('color'), 'rgba(255, 255, 255, 1)')

    def test_cult_section_explore_button(self):
        explore_button = self.driver.find_element(By.XPATH, "//div[@id='cult_section']//a[text()=' Explore ']")
        self.assertTrue(explore_button.is_displayed())
        self.assertTrue(explore_button.is_enabled())

if __name__ == "__main__":
    unittest.main()
