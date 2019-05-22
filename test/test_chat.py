# -*- coding: utf-8 -*-
import time
import unittest
from Python_testing_training.app.app import App


class TestAddText(unittest.TestCase):

    def setUp(self):
        self.app = App()

    def test_add_blue_text(self):
        self.app.go_page()
        self.app.enter_name('Test')
        self.app.enter_message('One Two Three')
        self.app.choose_color('blue')  # need to create functions for every color
        self.app.click_ok()

    def tearDown(self):
        self.app.destroy()
        pass


if __name__ == "__main__":
    unittest.main()
