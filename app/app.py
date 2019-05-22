from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from Python_testing_training import utils


class App:
    def __init__(self):
        self.URL = utils.get_project_root() + '\Python_testing_training\page_for_test.html'
        self.wd = webdriver.Chrome(ChromeDriverManager().install())

    def go_page(self):
        self.wd.get(self.URL)

    def enter_name(self, name):
        wd = self.wd
        wd.find_element_by_id('name').send_keys(name)

    def enter_message(self, msg):
        wd = self.wd
        wd.find_element_by_id('message').send_keys(msg)

    def choose_color(self, color):
        wd = self.wd
        wd.find_element_by_id(color).click()

    def click_ok(self):
        wd = self.wd
        wd.find_element_by_id('btn').click()

    def text_from_chat(self):
        pass

    def destroy(self):
        self.wd.quit()
