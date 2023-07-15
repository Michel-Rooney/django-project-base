from .base_home import HomeBaseFunctionalTest


class HomeTest(HomeBaseFunctionalTest):
    def test_home(self):
        self.browser.get('https://www.google.com/')
        self.sleep(5)
        self.assertEqual(1, 1)
