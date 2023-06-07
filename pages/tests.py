from django.test import TestCase, SimpleTestCase
from django.urls import reverse
# Create your tests here.
class HomePageTest(SimpleTestCase):
    def test_url_exist_cor_loc(self):
        response=self.client.get("/")
        self.assertEqual(response.status_code, 200)
    def test_url_exist_by_name(self):
        response=self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
    def test_correct_template_name(self):
        response=self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")
    def test_correct_content(self):
        response=self.client.get(reverse("home"))
        self.assertContains(response, "<h1>HomePage</h1>")



class AboutPageTest(SimpleTestCase):
    def test_url_exist_cor_loc(self):
        response=self.client.get("/about/")
        self.assertEqual(response.status_code, 200)
    def test_url_exist_by_name(self):
        response=self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)
    def test_correct_template_name(self):
        response=self.client.get(reverse("about"))
        self.assertTemplateUsed(response, "about.html")
    def test_correct_content(self):
        response=self.client.get(reverse("about"))
        self.assertContains(response, "<h1>About Page</h1>")