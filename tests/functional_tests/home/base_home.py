import time

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from utils.browser import make_edge_browser


class HomeBaseFunctionalTest(StaticLiveServerTestCase):
    def setUp(self) -> None:
        self.browser = make_edge_browser()
        return super().setUp()

    def tearDown(self) -> None:
        self.browser.quit()
        return super().tearDown()

    def sleep(self, seconds=5):
        time.sleep(seconds)
