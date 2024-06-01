from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class CultFitTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://act7-webap.azurewebsites.net/")  # Update with the correct path to your HTML file

    def test_page_title(self):
        self.assertEqual(self.driver.title, "Get Fitness Workouts, Gyms, Health Care, & Healthy Food in India by Cult.fit")

    def test_cult_section_content(self):
        cult_section = self.driver.find_element(By.ID, "cult_section")
        self.assertTrue(cult_section.is_displayed())

        slides = cult_section.find_elements(By.CSS_SELECTOR, "#cult_image_section ul li")
        self.assertEqual(len(slides), 3)

        slide1 = slides[0]
        self.assertTrue(slide1.find_element(By.CSS_SELECTOR, "img").is_displayed())
        self.assertTrue(slide1.find_element(By.CSS_SELECTOR, ".cult_btn").is_displayed())

    def test_footer_present(self):
        footer = self.driver.find_element(By.ID, "footer")
        self.assertTrue(footer.is_displayed())

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

