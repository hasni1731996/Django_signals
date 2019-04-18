from django.test import TestCase
from .models import *
from django.urls import reverse
import unittest
from selenium import webdriver
# models test
class FoodTest(TestCase):

    def create_food(self, name="only a test"):
        return Food.objects.create(name=name)

    def test_food_creation(self):
        w = self.create_food()
        self.assertTrue(isinstance(w, Food))
        self.assertEqual(w. __str__(), w.name)

    def test_food_list_view(self):
        w = self.create_food()
        url = reverse("cookbook.views.testing_view_func")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
        self.assertIn(w.title, resp.content)

class TestSignup(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_signup_fire(self):
        self.driver.get("http://localhost:8000/add/")
        self.driver.find_element_by_id('id_title').send_keys("test title")
        self.driver.find_element_by_id('id_body').send_keys("test body")
        self.driver.find_element_by_id('submit').click()
        self.assertIn("http://localhost:8000/", self.driver.current_url)

    def tearDown(self):
        self.driver.quit

if __name__ == '__main__':
    unittest.main()
